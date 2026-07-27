#!/usr/bin/env python3
"""Daily CrewAI pipeline for PostSingularity evidence research."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Sequence

from pydantic import Field

if __package__ in (None, ""):  # direct execution: python tools/research_crew.py
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.research_agent import (
    AssumptionAssessment,
    CanonImplication,
    DEFAULT_MODEL,
    Development,
    ResearchBrief,
    ResearchRun,
    Source,
    StrictModel,
    assumption_payload,
    build_parser,
    canon_payload,
    heading_index,
    require_openai_api_key,
    run_research_cli,
    validate_brief,
)


class EvidenceFinding(StrictModel):
    title: str
    observed_fact: str
    event_date: str
    significance: str
    limitations: list[str]
    sources: list[Source]


class EvidencePacket(StrictModel):
    focus: str
    findings: list[EvidenceFinding]
    search_gaps: list[str]


class AuditedEvidence(StrictModel):
    sources: list[Source]
    developments: list[Development]
    contradictions: list[str]
    quality_notes: list[str]
    excluded_claims: list[str]


class AnalysisPacket(StrictModel):
    assumption_assessments: list[AssumptionAssessment]
    uncertainties: list[str]
    watchlist: list[str]
    daily_change_summary: str = Field(
        description="What is meaningfully new since the prior state, without hype"
    )


class ImplementationPacket(StrictModel):
    canon_implications: list[CanonImplication]
    coverage_notes: list[str] = Field(
        description=(
            "Explanation for assessed assumptions that do not warrant a repository edit"
        )
    )


def crewai_model_name(model: str) -> str:
    """Normalize an OpenAI model for CrewAI's provider-prefixed format."""
    return model if "/" in model else f"openai/{model}"


DIRECTIONAL_VERDICTS = {"strengthened", "weakened", "contradicted", "mixed"}


def implementation_plan_errors(
    canon_implications: Sequence[CanonImplication],
    allowed_headings: dict[str, set[str]],
    selected_assumption_ids: set[str],
    known_source_ids: set[str],
    directional_ids: set[str],
) -> list[str]:
    """Deterministic checks the mapper must satisfy, shared by the guardrail.

    Mirrors ``validate_brief``'s constraints — including ``(path, heading)``
    uniqueness — so the mapper is corrected within its retry budget instead of
    passing the guardrail and then aborting the run at final validation.
    """
    errors: list[str] = []
    covered_assumptions: set[str] = set()
    seen_targets: set[tuple[str, str]] = set()
    for item in canon_implications:
        if item.path not in allowed_headings:
            errors.append(f"Unknown repository path: {item.path}")
            continue
        if item.target_heading.casefold() not in allowed_headings[item.path]:
            errors.append(f"Unknown heading in {item.path}: {item.target_heading}")
        target = (item.path, item.target_heading.casefold())
        if target in seen_targets:
            errors.append(
                f"Duplicate implementation target: {item.path} -> "
                f"{item.target_heading}. Merge findings for a heading into one "
                "item or anchor to a different existing heading."
            )
        seen_targets.add(target)
        unknown_assumptions = set(item.assumption_ids) - selected_assumption_ids
        if unknown_assumptions:
            errors.append(f"Unselected assumptions: {sorted(unknown_assumptions)}")
        covered_assumptions.update(item.assumption_ids)
        unknown_sources = set(item.source_ids) - known_source_ids
        if unknown_sources:
            errors.append(f"Unknown source IDs: {sorted(unknown_sources)}")
        if not item.implementation_steps:
            errors.append(
                f"{item.path} -> {item.target_heading} needs implementation steps"
            )

    uncovered = directional_ids - covered_assumptions
    if uncovered:
        errors.append(
            "Directional assumption assessments need implementation items: "
            f"{sorted(uncovered)}"
        )
    return errors


def build_research_crew(
    topic: str,
    lane: str,
    lookback_days: int,
    assumptions: Sequence[dict[str, Any]],
    canon_matches: Sequence[Any],
    model: str = DEFAULT_MODEL,
    reasoning_effort: str = "medium",
    verbose: bool = False,
) -> tuple[Any, Any]:
    """Construct the CrewAI crew and return it with its final task."""
    try:
        from crewai import Agent, Crew, LLM, Process, Task
    except ImportError as exc:
        raise RuntimeError(
            "CrewAI is not installed. Run "
            "'python -m pip install -r requirements-research-crew.txt -e .'."
        ) from exc

    model_name = crewai_model_name(model)
    research_llm = LLM(
        model=model_name,
        api="responses",
        builtin_tools=["web_search"],
        reasoning_effort=reasoning_effort,
        timeout=300,
        max_retries=2,
    )
    analysis_llm = LLM(
        model=model_name,
        api="responses",
        reasoning_effort=reasoning_effort,
        timeout=300,
        max_retries=2,
    )

    signal_scout = Agent(
        role="AI and Technology Signal Scout",
        goal=(
            "Find material, recent developments from primary and authoritative "
            "sources while separating measured results from announcements."
        ),
        backstory=(
            "You are a skeptical technology researcher. You search broadly, "
            "prefer exact dates and primary evidence, and ignore hype without "
            "measurable consequences."
        ),
        llm=research_llm,
        allow_delegation=False,
        verbose=verbose,
        max_iter=8,
    )
    counterevidence_scout = Agent(
        role="Counterevidence and Constraint Scout",
        goal=(
            "Find limitations, failed replications, deployment barriers, safety "
            "problems, and evidence that challenges optimistic interpretations."
        ),
        backstory=(
            "You are an adversarial research partner. Your job is not pessimism; "
            "it is preventing demonstrations, forecasts, and vendor claims from "
            "being mistaken for durable progress."
        ),
        llm=research_llm,
        allow_delegation=False,
        verbose=verbose,
        max_iter=8,
    )
    evidence_auditor = Agent(
        role="Evidence Auditor",
        goal=(
            "Deduplicate findings, check source quality and dates, reconcile "
            "conflicts, and produce a defensible evidence packet."
        ),
        backstory=(
            "You are a meticulous research-methods reviewer. You preserve "
            "uncertainty, reject unsupported URLs, and distinguish a laboratory "
            "result from real deployment."
        ),
        llm=analysis_llm,
        allow_delegation=False,
        verbose=verbose,
        max_iter=6,
    )
    assumption_analyst = Agent(
        role="PostSingularity Assumption Analyst",
        goal=(
            "Assess every selected assumption against audited evidence and state "
            "the real-world and storyworld implications without defending canon."
        ),
        backstory=(
            "You maintain a long-range forecast ledger. You use directional "
            "verdicts only when evidence warrants them and otherwise record "
            "insufficient evidence."
        ),
        llm=analysis_llm,
        allow_delegation=False,
        verbose=verbose,
        max_iter=6,
    )
    repository_mapper = Agent(
        role="PostSingularity Repository Implementation Mapper",
        goal=(
            "Translate reviewed evidence into exact, actionable repository edit "
            "plans tied to existing files, headings, assumptions, and source IDs."
        ),
        backstory=(
            "You are the storyworld's information architect and change planner. "
            "You understand that naming a nearby file is not enough: every proposal "
            "must identify the exact anchor, explain why it belongs there, describe "
            "the edit, and surface dependencies or canon conflicts."
        ),
        llm=analysis_llm,
        allow_delegation=False,
        verbose=verbose,
        max_iter=6,
    )
    canon_editor = Agent(
        role="Research Brief and Canon Review Editor",
        goal=(
            "Create a complete structured research brief for human review while "
            "leaving the assumption registry and canon unchanged."
        ),
        backstory=(
            "You are the final editor and provenance custodian. You preserve "
            "source IDs, include contradictions, and make conservative review "
            "recommendations rather than autonomous edits."
        ),
        llm=analysis_llm,
        allow_delegation=False,
        verbose=verbose,
        max_iter=6,
    )

    run_date = datetime.now(timezone.utc).date()
    start_date = run_date - timedelta(days=lookback_days)
    assumption_json = json.dumps(assumption_payload(assumptions), indent=2)
    canon_json = json.dumps(canon_payload(canon_matches), indent=2)

    signal_task = Task(
        description=f"""Independently research the most material developments for:
Topic: {topic}
Lane: {lane}
Priority window: {start_date.isoformat()} through {run_date.isoformat()}

Use web search. Prefer papers, standards, regulatory records, official technical
documentation, and first-party releases with measurable detail. Return roughly
five to eight findings, fewer when the evidence is thin. Every finding must
contain exact source URLs surfaced by search. Record publication/event dates,
limitations, and why the development matters. Do not analyze the storyworld yet.

Signals and assumptions that define relevance:
{assumption_json}""",
        expected_output=(
            "A structured EvidencePacket with recent facts, limitations, exact "
            "source URLs, and explicit search gaps."
        ),
        agent=signal_scout,
        output_pydantic=EvidencePacket,
    )
    counterevidence_task = Task(
        description=f"""Run a dedicated counterevidence search for the same topic:
Topic: {topic}
Lane: {lane}
Priority window: {start_date.isoformat()} through {run_date.isoformat()}

Search independently for failed replications, benchmark weaknesses, missing
deployment evidence, cost or scaling constraints, safety incidents, regulatory
barriers, and expert or primary evidence that narrows optimistic claims. Do not
merely summarize the first scout. Every factual finding needs an exact source URL.

Assumptions whose falsifiers matter:
{assumption_json}""",
        expected_output=(
            "A structured EvidencePacket containing the strongest challenges, "
            "constraints, contradictory evidence, and remaining search gaps."
        ),
        agent=counterevidence_scout,
        output_pydantic=EvidencePacket,
    )
    audit_task = Task(
        description="""Audit both evidence packets. Deduplicate sources and
findings, renumber sources as S1, S2, and so on, and ensure every development
references valid source IDs. Prefer primary evidence. Identify conflicts,
company-only claims, forecasts, demonstrations without deployment evidence, and
claims that should be excluded. Do not invent replacement sources or URLs.""",
        expected_output=(
            "An AuditedEvidence object with a clean source list, source-linked "
            "developments, contradictions, quality notes, and excluded claims."
        ),
        agent=evidence_auditor,
        context=[signal_task, counterevidence_task],
        output_pydantic=AuditedEvidence,
    )
    analysis_task = Task(
        description=f"""Assess every supplied assumption ID against the audited
evidence. Return exactly one assessment per assumption. A lack of evidence must
produce an insufficient-evidence verdict, not omission. Separate the real-world
implication from the PostSingularity implication. Concentrate on the strength
and direction of evidence; the repository mapper will decide where changes belong.

Tracked assumptions:
{assumption_json}""",
        expected_output=(
            "An AnalysisPacket covering every selected assumption, uncertainty, "
            "a watchlist, and a sober daily change summary."
        ),
        agent=assumption_analyst,
        context=[audit_task],
        output_pydantic=AnalysisPacket,
    )

    allowed_headings = heading_index(canon_matches)
    selected_assumption_ids = {assumption["id"] for assumption in assumptions}

    def implementation_guardrail(task_output):
        packet = task_output.pydantic
        if not isinstance(packet, ImplementationPacket):
            return False, "Return a valid typed ImplementationPacket."

        # Sequential process guarantees audit_task/analysis_task have run first.
        known_source_ids: set[str] = set()
        if audit_task.output and isinstance(audit_task.output.pydantic, AuditedEvidence):
            known_source_ids = {
                source.id for source in audit_task.output.pydantic.sources
            }

        directional_ids: set[str] = set()
        if analysis_task.output and isinstance(
            analysis_task.output.pydantic, AnalysisPacket
        ):
            directional_ids = {
                assessment.assumption_id
                for assessment in analysis_task.output.pydantic.assumption_assessments
                if assessment.verdict in DIRECTIONAL_VERDICTS
            }

        errors = implementation_plan_errors(
            packet.canon_implications,
            allowed_headings,
            selected_assumption_ids,
            known_source_ids,
            directional_ids,
        )
        if errors:
            return False, "Repository mapping errors: " + "; ".join(errors)
        return True, task_output

    mapping_task = Task(
        description=f"""Convert the audited evidence and assumption assessments
into an actionable repository implementation plan.

Repository context:
{canon_json}

Requirements:
- Prefer files declared for the affected assumption before discovered related files.
- Use only repository paths supplied above.
- Copy target_heading exactly from that file's existing_headings list. Use the
  closest existing heading as the insertion anchor when proposing a new subsection.
- Cite the exact assumption IDs and audited source IDs that justify each plan item.
- State whether evidence supports, challenges, qualifies, extends, or has no
  material effect on the target content.
- proposed_change must describe the actual content to add, remove, or qualify.
  Generic language such as "update this file to reflect the evidence" is invalid.
- implementation_steps must explain placement, cross-references, metadata or index
  effects, and review order where relevant.
- dependencies_or_conflicts must identify related canon claims, chronology,
  terminology, or narrative consequences that a human reviewer should reconcile.
- Give high priority only to strong, material contradictions or time-sensitive
  updates. Use no-change/watch when the evidence is insufficient.
- Cover every directional or mixed assumption assessment with at least one plan
  item. Explain non-actionable assessments in coverage_notes.
- Do not edit files and do not claim that any proposal has been accepted.""",
        expected_output=(
            "An ImplementationPacket containing exact file-and-heading edit plans "
            "plus coverage notes for assumptions that do not warrant a change."
        ),
        agent=repository_mapper,
        context=[audit_task, analysis_task],
        output_pydantic=ImplementationPacket,
        guardrail=implementation_guardrail,
        guardrail_max_retries=2,
    )
    editor_task = Task(
        description=f"""Assemble the final structured ResearchBrief from the
audited evidence and assumption analysis.

Topic: {topic}
Lane: {lane}
Research window: {start_date.isoformat()} through {run_date.isoformat()}

Requirements:
- Preserve the auditor's exact source IDs and URLs.
- Include the audited developments and every assumption assessment.
- Preserve the repository mapper's implementation items without weakening their
  file, heading, evidence, proposed-change, dependency, or priority detail.
- Carry repository-mapper coverage notes into uncertainties when no edit is warranted.
- Include contradictions and excluded-claim concerns in uncertainties.
- Make the title and executive summary decision-useful, not promotional.
- Use only these repository paths and headings for canon implications:
{canon_json}
- Do not modify canon or claim that the registry was updated.""",
        expected_output=(
            "A complete ResearchBrief Pydantic object ready for deterministic "
            "validation and Markdown rendering."
        ),
        agent=canon_editor,
        context=[audit_task, analysis_task, mapping_task],
        output_pydantic=ResearchBrief,
    )

    crew = Crew(
        agents=[
            signal_scout,
            counterevidence_scout,
            evidence_auditor,
            assumption_analyst,
            repository_mapper,
            canon_editor,
        ],
        tasks=[
            signal_task,
            counterevidence_task,
            audit_task,
            analysis_task,
            mapping_task,
            editor_task,
        ],
        process=Process.sequential,
        verbose=verbose,
        memory=False,
        planning=False,
    )
    return crew, editor_task


def run_crew_research(
    topic: str,
    lane: str,
    lookback_days: int,
    assumptions: Sequence[dict[str, Any]],
    canon_matches: Sequence[Any],
    model: str,
    reasoning_effort: str,
    verbose: bool,
) -> ResearchBrief:
    require_openai_api_key()
    crew, editor_task = build_research_crew(
        topic,
        lane,
        lookback_days,
        assumptions,
        canon_matches,
        model,
        reasoning_effort,
        verbose,
    )
    crew.kickoff()
    if editor_task.output is None:
        raise RuntimeError("CrewAI completed without a final task output")
    if editor_task.output.pydantic is not None:
        brief = ResearchBrief.model_validate(editor_task.output.pydantic)
    else:
        brief = ResearchBrief.model_validate_json(editor_task.output.raw)
    validate_brief(brief, assumptions, canon_matches)
    return brief


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    parser.prog = "postsingularity-research-crew"
    parser.description = (
        "Run the daily CrewAI research team against tracked PostSingularity assumptions."
    )
    parser.add_argument(
        "--verbose-crew",
        action="store_true",
        help="Show CrewAI agent and task execution details",
    )
    args = parser.parse_args(argv)
    if args.lookback_days < 1:
        parser.error("--lookback-days must be at least 1")

    def live_runner(run: ResearchRun) -> tuple[ResearchBrief, set[str]]:
        brief = run_crew_research(
            run.topic,
            run.lane,
            run.lookback_days,
            run.assumptions,
            run.canon_matches,
            args.model,
            args.reasoning_effort,
            args.verbose_crew,
        )
        return brief, set()

    return run_research_cli(
        args,
        live_runner,
        f"CrewAI/{args.model}",
        "research crew error",
    )


if __name__ == "__main__":
    raise SystemExit(main())

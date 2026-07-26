#!/usr/bin/env python3
"""Daily CrewAI pipeline for PostSingularity evidence research."""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timedelta, timezone
from typing import Any, Sequence

from pydantic import Field

from tools.research_agent import (
    AssumptionAssessment,
    CanonImplication,
    DEFAULT_MODEL,
    Development,
    ResearchBrief,
    Source,
    StrictModel,
    append_submission_log,
    build_mock_brief,
    build_parser,
    format_memo,
    infer_lane,
    load_assumptions,
    load_canon_files,
    nearby_canon,
    scheduled_topic,
    select_assumptions,
    validate_brief,
    write_memo,
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
    canon_implications: list[CanonImplication]
    uncertainties: list[str]
    watchlist: list[str]
    daily_change_summary: str = Field(
        description="What is meaningfully new since the prior state, without hype"
    )


def crewai_model_name(model: str) -> str:
    """Normalize an OpenAI model for CrewAI's provider-prefixed format."""
    return model if "/" in model else f"openai/{model}"


def _selected_assumption_json(assumptions: Sequence[dict[str, Any]]) -> str:
    fields = (
        "id",
        "title",
        "claim",
        "kind",
        "horizon",
        "status",
        "canon_sources",
        "signals_to_watch",
        "falsifiers",
    )
    return json.dumps(
        [{field: item.get(field) for field in fields} for item in assumptions],
        indent=2,
    )


def _canon_context_json(canon_matches: Sequence[Any]) -> str:
    return json.dumps(
        [
            {
                "path": match.path,
                "title": match.title,
                "why_nearby": match.reason,
                "excerpt": match.excerpt,
            }
            for match in canon_matches
        ],
        indent=2,
    )


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
    assumption_json = _selected_assumption_json(assumptions)
    canon_json = _canon_context_json(canon_matches)

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
implication from the PostSingularity implication. Recommend only monitor,
revise, debate, or no-change for canon.

Tracked assumptions:
{assumption_json}

Nearby canon:
{canon_json}""",
        expected_output=(
            "An AnalysisPacket covering every selected assumption, canon review "
            "implications, uncertainty, a watchlist, and a sober daily change summary."
        ),
        agent=assumption_analyst,
        context=[audit_task],
        output_pydantic=AnalysisPacket,
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
- Include contradictions and excluded-claim concerns in uncertainties.
- Make the title and executive summary decision-useful, not promotional.
- Use only these nearby canon paths for canon implications:
{canon_json}
- Do not modify canon or claim that the registry was updated.""",
        expected_output=(
            "A complete ResearchBrief Pydantic object ready for deterministic "
            "validation and Markdown rendering."
        ),
        agent=canon_editor,
        context=[audit_task, analysis_task],
        output_pydantic=ResearchBrief,
    )

    crew = Crew(
        agents=[
            signal_scout,
            counterevidence_scout,
            evidence_auditor,
            assumption_analyst,
            canon_editor,
        ],
        tasks=[
            signal_task,
            counterevidence_task,
            audit_task,
            analysis_task,
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
    if not os.environ.get("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Configure it or use --mock for a non-API run."
        )
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
    validate_brief(brief, assumptions)
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

    try:
        assumptions = load_assumptions(args.assumptions_file)
        if args.list_assumptions:
            for item in assumptions:
                print(f"{item['id']}\t{item['lane']}\t{item['status']}\t{item['title']}")
            return 0

        run_date = datetime.now(timezone.utc).date()
        if args.topic:
            topic = args.topic.strip()
            lane = infer_lane(topic, assumptions) if args.lane == "auto" else args.lane
        else:
            lane, topic = scheduled_topic(run_date, args.lane)

        selected = select_assumptions(
            topic,
            lane,
            assumptions,
            requested_ids=args.assumption,
        )
        canon_matches = nearby_canon(topic, lane, load_canon_files(), limit=6)

        if args.mock:
            brief = build_mock_brief(
                topic,
                lane,
                selected,
                canon_matches,
                run_date,
                args.lookback_days,
            )
        else:
            brief = run_crew_research(
                topic,
                lane,
                args.lookback_days,
                selected,
                canon_matches,
                args.model,
                args.reasoning_effort,
                args.verbose_crew,
            )

        markdown = format_memo(
            brief,
            topic,
            selected,
            canon_matches,
            run_date,
            f"CrewAI/{args.model}",
            args.mock,
        )
        if args.dry_run:
            print(markdown)
            return 0

        report_path = write_memo(markdown, topic, lane, args.output_dir, run_date)
        if not args.no_log:
            append_submission_log(args.submissions_log, report_path, topic)
        print(report_path)
        return 0
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"research crew error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

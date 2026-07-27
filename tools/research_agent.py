#!/usr/bin/env python3
"""Research real-world signals against PostSingularity assumptions.

The agent searches current sources through the OpenAI Responses API, maps
evidence to explicit assumptions and nearby canon, and writes a non-canonical
Markdown brief for human review.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Iterable, Literal, Sequence

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, field_validator

if __package__ in (None, ""):  # direct execution: python tools/research_agent.py
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.markdown_utils import extract_headings, extract_title, parse_tags


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ASSUMPTIONS_PATH = REPO_ROOT / "research" / "assumptions.json"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "pending-review" / "agent-research"
DEFAULT_SUBMISSIONS_LOG = REPO_ROOT / "submissions-log.md"
DEFAULT_MODEL = "gpt-5.6-luna"

Lane = Literal[
    "ai",
    "robotics",
    "neurotechnology",
    "biotechnology",
    "energy",
    "space",
    "governance",
    "social-systems",
]
Verdict = Literal[
    "strengthened",
    "weakened",
    "contradicted",
    "unchanged",
    "mixed",
    "insufficient-evidence",
]
Confidence = Literal["low", "medium", "high"]

LANES: dict[str, dict[str, Any]] = {
    "ai": {
        "topic": "AI capabilities, agents, alignment, evaluation, and research automation",
        "preferred_roots": ["worldbible/technologies", "philosophy"],
        "keywords": ["ai", "agent", "model", "alignment", "automation", "intelligence"],
    },
    "robotics": {
        "topic": "general-purpose robotics, dexterity, robot learning, and autonomous logistics",
        "preferred_roots": ["worldbible/technologies", "locations"],
        "keywords": ["robot", "drone", "autonomous", "logistics", "embodied"],
    },
    "neurotechnology": {
        "topic": "brain-computer interfaces, neurostimulation, neural decoding, and neuro-rights",
        "preferred_roots": ["worldbible/technologies", "philosophy"],
        "keywords": ["neural", "brain", "emotion", "sensory", "neuro"],
    },
    "biotechnology": {
        "topic": "biofabrication, synthetic biology, cellular agriculture, and human enhancement",
        "preferred_roots": ["worldbible/technologies", "philosophy"],
        "keywords": ["bio", "fabrication", "cell", "organic", "health"],
    },
    "energy": {
        "topic": "clean energy abundance, storage, fusion, grids, and distributed generation",
        "preferred_roots": ["worldbible/technologies", "locations"],
        "keywords": ["energy", "solar", "fusion", "grid", "storage", "geothermal"],
    },
    "space": {
        "topic": "space habitation, launch systems, life support, and autonomous missions",
        "preferred_roots": ["worldbible/technologies", "locations"],
        "keywords": ["space", "orbital", "aerospace", "habitat", "propulsion"],
    },
    "governance": {
        "topic": "AI governance, collective intelligence, provenance, regulation, and public legitimacy",
        "preferred_roots": ["worldbible/technologies", "philosophy", "protocols"],
        "keywords": ["governance", "trust", "audit", "provenance", "consent", "public"],
    },
    "social-systems": {
        "topic": "automation, future of work, meaning, digital resistance, and social adaptation",
        "preferred_roots": ["philosophy", "worldbible", "protocols", "stories"],
        "keywords": ["society", "work", "meaning", "analog", "culture", "identity"],
    },
}

CANON_ROOTS = (
    "worldbible",
    "philosophy",
    "protocols",
    "characters",
    "locations",
    "stories",
)
STOPWORDS = {
    "about",
    "after",
    "against",
    "become",
    "between",
    "could",
    "from",
    "have",
    "into",
    "more",
    "that",
    "their",
    "these",
    "they",
    "this",
    "through",
    "toward",
    "under",
    "when",
    "where",
    "which",
    "with",
    "would",
}


@dataclass(frozen=True)
class CanonDocument:
    path: str
    title: str
    tags: tuple[str, ...]
    content: str


@dataclass(frozen=True)
class CanonMatch:
    path: str
    title: str
    reason: str
    score: int
    excerpt: str
    headings: tuple[str, ...] = ()
    assumption_ids: tuple[str, ...] = ()


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Source(StrictModel):
    id: str = Field(description="Short stable identifier such as S1")
    title: str
    url: str = Field(
        pattern=r"^https?://",
        description="Absolute HTTP or HTTPS source URL",
    )
    publisher: str
    published_at: str = Field(description="ISO date when known, otherwise 'unknown'")
    source_type: Literal[
        "primary-research",
        "official-release",
        "standard",
        "regulatory",
        "reputable-secondary",
        "mock",
    ]
    why_relevant: str

    @field_validator("url")
    @classmethod
    def normalize_url(cls, value: str) -> str:
        """Keep validated URLs JSON-native for CrewAI task persistence."""
        return str(HttpUrl(value))


class Development(StrictModel):
    title: str
    observed_fact: str
    event_date: str = Field(description="ISO date when known, otherwise 'unknown'")
    source_ids: list[str]
    significance: str


class AssumptionAssessment(StrictModel):
    assumption_id: str
    verdict: Verdict
    confidence: Confidence
    evidence_summary: str
    real_world_implication: str
    post_singularity_implication: str
    source_ids: list[str]


class CanonImplication(StrictModel):
    path: str
    target_heading: str = Field(
        description="Exact existing Markdown heading used as the edit anchor"
    )
    assumption_ids: list[str] = Field(min_length=1)
    source_ids: list[str] = Field(min_length=1)
    relationship: Literal[
        "supports",
        "challenges",
        "qualifies",
        "extends",
        "no-material-effect",
    ]
    recommendation: Literal["monitor", "revise", "debate", "no-change"]
    priority: Literal["high", "medium", "low", "watch"]
    rationale: str = Field(min_length=20)
    proposed_change: str = Field(
        min_length=30,
        description="Concrete content change or explicit reason to leave the file unchanged"
    )
    implementation_steps: list[str] = Field(min_length=1)
    dependencies_or_conflicts: list[str]


class ResearchBrief(StrictModel):
    title: str
    executive_summary: str
    lane: Lane
    research_window: str
    developments: list[Development]
    assumption_assessments: list[AssumptionAssessment]
    canon_implications: list[CanonImplication]
    uncertainties: list[str]
    watchlist: list[str]
    sources: list[Source]


def slugify(value: str) -> str:
    """Return a lowercase, filesystem-safe slug."""
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value or "research-brief"


def tokenize(value: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9][a-z0-9-]{2,}", value.lower())
        if token not in STOPWORDS
    }


def relevant_excerpt(
    content: str,
    query_tokens: set[str],
    max_chars: int = 2200,
) -> str:
    """Select the most query-relevant Markdown sections for repository mapping."""
    sections = [
        section.strip()
        for section in re.split(r"(?=^#{1,6}\s+)", content, flags=re.MULTILINE)
        if section.strip()
    ]
    ranked: list[tuple[int, int, str]] = []
    for index, section in enumerate(sections):
        section_tokens = tokenize(section)
        heading_match = re.match(r"^#{1,6}\s+(.+)$", section, re.MULTILINE)
        heading_tokens = tokenize(heading_match.group(1)) if heading_match else set()
        score = len(query_tokens & heading_tokens) * 5 + len(
            query_tokens & section_tokens
        )
        ranked.append((score, -index, re.sub(r"\s+", " ", section).strip()))

    ranked.sort(reverse=True)
    selected: list[str] = []
    total = 0
    for _, _, section in ranked:
        if selected and total + len(section) > max_chars:
            continue
        selected.append(section)
        total += len(section)
        if total >= max_chars or len(selected) >= 4:
            break
    return "\n\n".join(selected)[:max_chars]


def load_canon_files(repo_root: Path = REPO_ROOT) -> list[CanonDocument]:
    """Load human-authored canon and narrative Markdown files."""
    documents: list[CanonDocument] = []
    overview = repo_root / "README.md"
    if overview.is_file():
        text = overview.read_text(encoding="utf-8")
        documents.append(
            CanonDocument(
                path="README.md",
                title=extract_title(text, "PostSingularity"),
                tags=parse_tags(text),
                content=text,
            )
        )
    for root_name in CANON_ROOTS:
        root = repo_root / root_name
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            documents.append(
                CanonDocument(
                    path=path.relative_to(repo_root).as_posix(),
                    title=extract_title(text, path.stem.replace("-", " ").title()),
                    tags=parse_tags(text),
                    content=text,
                )
            )
    return documents


def nearby_canon(
    topic: str,
    lane: str,
    documents: Sequence[CanonDocument],
    limit: int = 6,
) -> list[CanonMatch]:
    """Rank canon by topic overlap, tags, and lane-aware directory preference."""
    query_tokens = tokenize(topic) | set(LANES[lane]["keywords"])
    preferred_roots = tuple(LANES[lane]["preferred_roots"])
    ranked: list[CanonMatch] = []

    for document in documents:
        title_tokens = tokenize(document.title)
        tag_tokens = tokenize(" ".join(document.tags))
        content_tokens = tokenize(document.content)
        title_hits = sorted(query_tokens & title_tokens)
        tag_hits = sorted(query_tokens & tag_tokens)
        content_hits = sorted(query_tokens & content_tokens)
        preferred = document.path.startswith(preferred_roots)
        score = len(title_hits) * 6 + len(tag_hits) * 4 + min(len(content_hits), 8)
        if preferred:
            score += 3
        if score <= 0:
            continue

        reasons = []
        if title_hits:
            reasons.append(f"title: {', '.join(title_hits[:4])}")
        if tag_hits:
            reasons.append(f"tags: {', '.join(tag_hits[:4])}")
        if content_hits:
            reasons.append(f"content: {', '.join(content_hits[:4])}")
        if preferred:
            reasons.append(f"{lane} directory preference")
        excerpt = relevant_excerpt(document.content, query_tokens)
        ranked.append(
            CanonMatch(
                path=document.path,
                title=document.title,
                reason="; ".join(reasons),
                score=score,
                excerpt=excerpt,
                headings=extract_headings(document.content),
            )
        )

    ranked.sort(key=lambda item: (-item.score, item.path))
    return ranked[:limit]


def select_canon_context(
    topic: str,
    lane: str,
    documents: Sequence[CanonDocument],
    assumptions: Sequence[dict[str, Any]],
    limit: int = 12,
) -> list[CanonMatch]:
    """Combine declared assumption canon with discovered related repository files."""
    documents_by_path = {document.path: document for document in documents}
    assumption_ids_by_path: dict[str, list[str]] = {}
    for assumption in assumptions:
        for path in assumption["canon_sources"]:
            assumption_ids_by_path.setdefault(path, []).append(assumption["id"])

    declared: list[CanonMatch] = []
    for path, assumption_ids in assumption_ids_by_path.items():
        document = documents_by_path.get(path)
        if document is None:
            raise ValueError(f"Declared canon source was not loaded: {path}")
        related_assumptions = [
            assumption for assumption in assumptions if assumption["id"] in assumption_ids
        ]
        query_tokens = tokenize(
            " ".join(
                [
                    topic,
                    *[
                        " ".join(
                            [
                                assumption["title"],
                                assumption["claim"],
                                " ".join(assumption["keywords"]),
                            ]
                        )
                        for assumption in related_assumptions
                    ],
                ]
            )
        )
        declared.append(
            CanonMatch(
                path=path,
                title=document.title,
                reason=(
                    "declared canon source for " + ", ".join(sorted(assumption_ids))
                ),
                score=10_000,
                excerpt=relevant_excerpt(document.content, query_tokens),
                headings=extract_headings(document.content),
                assumption_ids=tuple(sorted(assumption_ids)),
            )
        )

    discovered = nearby_canon(topic, lane, documents, limit=limit)
    selected = list(declared)
    seen = {match.path for match in declared}
    for match in discovered:
        if match.path in seen:
            continue
        selected.append(match)
        seen.add(match.path)
        if len(selected) >= max(limit, len(declared)):
            break
    return selected


def load_assumptions(path: Path = DEFAULT_ASSUMPTIONS_PATH) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    assumptions = payload.get("assumptions")
    if not isinstance(assumptions, list) or not assumptions:
        raise ValueError(f"No assumptions found in {path}")

    required = {
        "id",
        "title",
        "claim",
        "kind",
        "lane",
        "status",
        "canon_sources",
        "keywords",
        "signals_to_watch",
        "falsifiers",
    }
    seen: set[str] = set()
    for assumption in assumptions:
        missing = required - assumption.keys()
        if missing:
            raise ValueError(f"{assumption.get('id', '<unknown>')} is missing {sorted(missing)}")
        if assumption["id"] in seen:
            raise ValueError(f"Duplicate assumption ID: {assumption['id']}")
        if assumption["lane"] not in LANES:
            raise ValueError(f"Unknown lane for {assumption['id']}: {assumption['lane']}")
        seen.add(assumption["id"])
    return assumptions


def infer_lane(topic: str, assumptions: Sequence[dict[str, Any]]) -> str:
    topic_tokens = tokenize(topic)
    scores: dict[str, int] = {}
    for lane, config in LANES.items():
        scores[lane] = len(topic_tokens & set(config["keywords"])) * 4
    for assumption in assumptions:
        assumption_tokens = tokenize(
            " ".join(
                [
                    assumption["title"],
                    assumption["claim"],
                    " ".join(assumption["keywords"]),
                ]
            )
        )
        scores[assumption["lane"]] += len(topic_tokens & assumption_tokens)
    return max(LANES, key=lambda lane: (scores[lane], -list(LANES).index(lane)))


def scheduled_topic(run_date: date, requested_lane: str = "auto") -> tuple[str, str]:
    """Choose a deterministic weekly lane and topic."""
    if requested_lane == "auto":
        lane_names = list(LANES)
        lane = lane_names[run_date.isocalendar().week % len(lane_names)]
    else:
        lane = requested_lane
    return lane, LANES[lane]["topic"]


def select_assumptions(
    topic: str,
    lane: str,
    assumptions: Sequence[dict[str, Any]],
    requested_ids: Sequence[str] = (),
    limit: int = 5,
) -> list[dict[str, Any]]:
    by_id = {item["id"]: item for item in assumptions}
    unknown = [item_id for item_id in requested_ids if item_id not in by_id]
    if unknown:
        raise ValueError(f"Unknown assumption ID(s): {', '.join(unknown)}")
    if requested_ids:
        return [by_id[item_id] for item_id in requested_ids]

    query_tokens = tokenize(topic) | set(LANES[lane]["keywords"])
    ranked: list[tuple[int, str, dict[str, Any]]] = []
    for assumption in assumptions:
        title_tokens = tokenize(assumption["title"])
        keyword_tokens = tokenize(" ".join(assumption["keywords"]))
        claim_tokens = tokenize(assumption["claim"])
        score = (
            len(query_tokens & title_tokens) * 5
            + len(query_tokens & keyword_tokens) * 3
            + len(query_tokens & claim_tokens)
        )
        if assumption["lane"] == lane:
            score += 8
        ranked.append((score, assumption["id"], assumption))
    ranked.sort(key=lambda item: (-item[0], item[1]))
    return [item[2] for item in ranked[:limit]]


ASSUMPTION_PAYLOAD_FIELDS = (
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


def assumption_payload(
    assumptions: Sequence[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Return the prompt-facing view of tracked assumptions."""
    return [
        {field: item.get(field) for field in ASSUMPTION_PAYLOAD_FIELDS}
        for item in assumptions
    ]


def canon_payload(canon_matches: Sequence[CanonMatch]) -> list[dict[str, Any]]:
    """Return the prompt-facing view of nearby canon."""
    return [
        {
            "path": match.path,
            "title": match.title,
            "why_nearby": match.reason,
            "declared_for_assumptions": list(match.assumption_ids),
            "existing_headings": list(match.headings),
            "excerpt": match.excerpt,
        }
        for match in canon_matches
    ]


def heading_index(canon_matches: Sequence[CanonMatch]) -> dict[str, set[str]]:
    """Map each supplied canon path to its case-folded headings."""
    return {
        match.path: {heading.casefold() for heading in match.headings}
        for match in canon_matches
    }


def require_openai_api_key() -> None:
    if not os.environ.get("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Configure it or use --mock for a non-API run."
        )


def build_prompt(
    topic: str,
    lane: str,
    lookback_days: int,
    assumptions: Sequence[dict[str, Any]],
    canon_matches: Sequence[CanonMatch],
    run_date: date,
) -> list[dict[str, str]]:
    start_date = run_date - timedelta(days=lookback_days)
    system = """You are the evidence analyst for the PostSingularity speculative
storyworld. Search the web and evaluate real developments without trying to
defend the fiction.

Keep these boundaries:
- Prefer primary research, official documentation, standards, regulatory
  records, and first-party releases. Use reputable secondary reporting only
  when it adds necessary context.
- Separate observed facts from inference. A demo is not a deployment; a company
  claim is not independent validation; a forecast is not an observed result.
- Every material factual claim must reference one or more source IDs, and every
  source must have the exact URL surfaced by web research.
- Assess only the supplied assumption IDs. Use "insufficient-evidence" when the
  available evidence does not justify a directional verdict.
- Turn canon review into an implementation plan: use only supplied repository
  paths, anchor each proposal to an exact supplied heading, cite the assumption
  and evidence IDs, and state concrete edit steps and conflicts.
- Prefer each assumption's declared canon sources before adding discovered
  related files. Never claim to modify canon.
- Include contradictory evidence and meaningful uncertainty.
- Return only data conforming to the provided structured-output schema."""
    user = f"""Research topic: {topic}
Research lane: {lane}
Current date: {run_date.isoformat()}
Primary lookback window: {start_date.isoformat()} through {run_date.isoformat()}

Prioritize developments inside the lookback window. Older evidence is allowed
only when it is necessary to interpret a recent development.

Tracked assumptions:
{json.dumps(assumption_payload(assumptions), indent=2)}

Nearby PostSingularity canon:
{json.dumps(canon_payload(canon_matches), indent=2)}

Produce a decision-useful research brief. Explain what changed, how strong the
evidence is, which assumptions are strengthened or weakened, and exactly where
and how accepted evidence could be implemented in the repository. Generic
instructions such as "revise this file" are insufficient."""
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


def extract_native_citations(response: Any) -> set[str]:
    """Collect URL citations from a Responses API object without SDK coupling."""
    try:
        payload = response.model_dump(mode="json")
    except AttributeError:
        return set()

    urls: set[str] = set()

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            if value.get("type") == "url_citation":
                url = value.get("url")
                if not url and isinstance(value.get("url_citation"), dict):
                    url = value["url_citation"].get("url")
                if isinstance(url, str):
                    urls.add(url)
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(payload)
    return urls


def validate_brief(
    brief: ResearchBrief,
    selected_assumptions: Sequence[dict[str, Any]],
    canon_matches: Sequence[CanonMatch] = (),
) -> None:
    source_ids = [source.id for source in brief.sources]
    if not source_ids:
        raise ValueError("The research response did not include any sources")
    if len(source_ids) != len(set(source_ids)):
        raise ValueError("The research response contains duplicate source IDs")

    known_sources = set(source_ids)
    for development in brief.developments:
        missing = set(development.source_ids) - known_sources
        if missing:
            raise ValueError(f"{development.title} cites unknown sources: {sorted(missing)}")

    selected_ids = {item["id"] for item in selected_assumptions}
    for assessment in brief.assumption_assessments:
        if assessment.assumption_id not in selected_ids:
            raise ValueError(f"Response assessed unselected assumption {assessment.assumption_id}")
        missing = set(assessment.source_ids) - known_sources
        if missing:
            raise ValueError(
                f"{assessment.assumption_id} cites unknown sources: {sorted(missing)}"
            )

    allowed_headings = heading_index(canon_matches)
    seen_targets: set[tuple[str, str]] = set()
    for implication in brief.canon_implications:
        if allowed_headings and implication.path not in allowed_headings:
            raise ValueError(
                f"Canon plan references a file outside supplied context: {implication.path}"
            )
        unknown_assumptions = set(implication.assumption_ids) - selected_ids
        if unknown_assumptions:
            raise ValueError(
                "Canon plan references unselected assumptions: "
                f"{sorted(unknown_assumptions)}"
            )
        missing_sources = set(implication.source_ids) - known_sources
        if missing_sources:
            raise ValueError(
                f"Canon plan for {implication.path} cites unknown sources: "
                f"{sorted(missing_sources)}"
            )
        if allowed_headings:
            if implication.target_heading.casefold() not in allowed_headings[implication.path]:
                raise ValueError(
                    f"Unknown target heading in {implication.path}: "
                    f"{implication.target_heading}"
                )
        target = (implication.path, implication.target_heading.casefold())
        if target in seen_targets:
            raise ValueError(f"Duplicate canon implementation target: {target}")
        seen_targets.add(target)


def run_live_research(
    topic: str,
    lane: str,
    lookback_days: int,
    assumptions: Sequence[dict[str, Any]],
    canon_matches: Sequence[CanonMatch],
    run_date: date,
    model: str,
    reasoning_effort: str,
) -> tuple[ResearchBrief, set[str]]:
    require_openai_api_key()

    from openai import OpenAI

    client = OpenAI()
    response = client.responses.parse(
        model=model,
        reasoning={"effort": reasoning_effort},
        tools=[{"type": "web_search"}],
        input=build_prompt(
            topic,
            lane,
            lookback_days,
            assumptions,
            canon_matches,
            run_date,
        ),
        text_format=ResearchBrief,
    )
    if response.output_parsed is None:
        raise RuntimeError("The model returned no parsed research brief")
    brief = response.output_parsed
    validate_brief(brief, assumptions, canon_matches)
    return brief, extract_native_citations(response)


def build_mock_brief(
    topic: str,
    lane: str,
    assumptions: Sequence[dict[str, Any]],
    canon_matches: Sequence[CanonMatch],
    run_date: date,
    lookback_days: int,
) -> ResearchBrief:
    """Build deterministic synthetic data for formatting and workflow tests."""
    assumption = assumptions[0]
    canon_match = canon_matches[0] if canon_matches else None
    canon_path = canon_match.path if canon_match else assumption["canon_sources"][0]
    target_heading = (
        canon_match.headings[0]
        if canon_match and canon_match.headings
        else "PostSingularity"
    )
    return ResearchBrief(
        title=f"Mock research brief: {topic}",
        executive_summary=(
            "Synthetic output used to verify the local pipeline. It is not real "
            "research and must not be used to update an assumption or canon."
        ),
        lane=lane,
        research_window=(
            f"{(run_date - timedelta(days=lookback_days)).isoformat()} "
            f"through {run_date.isoformat()}"
        ),
        developments=[
            Development(
                title="Synthetic pipeline verification signal",
                observed_fact="Mock mode generated this record without calling an API.",
                event_date=run_date.isoformat(),
                source_ids=["S1"],
                significance="Confirms structured formatting and file generation only.",
            )
        ],
        assumption_assessments=[
            AssumptionAssessment(
                assumption_id=assumption["id"],
                verdict="insufficient-evidence",
                confidence="low",
                evidence_summary="Mock data cannot provide evidence.",
                real_world_implication="No real-world conclusion is available.",
                post_singularity_implication="Do not change the tracked premise or canon.",
                source_ids=["S1"],
            )
        ],
        canon_implications=[
            CanonImplication(
                path=canon_path,
                target_heading=target_heading,
                assumption_ids=[assumption["id"]],
                source_ids=["S1"],
                relationship="no-material-effect",
                recommendation="no-change",
                priority="watch",
                rationale="Mock evidence cannot justify a repository change.",
                proposed_change=(
                    "Leave the target section unchanged until live evidence is reviewed."
                ),
                implementation_steps=[
                    "Run a live source-grounded research pass.",
                    "Reassess this exact section after human source verification.",
                ],
                dependencies_or_conflicts=[
                    "Synthetic fixtures must never be treated as canon evidence."
                ],
            )
        ],
        uncertainties=["All substantive content in this report is synthetic."],
        watchlist=["Run a live, source-grounded research pass after configuring the API key."],
        sources=[
            Source(
                id="S1",
                title="Synthetic source for mock mode",
                url="https://example.invalid/postsingularity-research-mock",
                publisher="PostSingularity test fixture",
                published_at=run_date.isoformat(),
                source_type="mock",
                why_relevant="Exercises source formatting without representing evidence.",
            )
        ],
    )


def _bullets(items: Iterable[str], empty: str = "None recorded.") -> list[str]:
    values = [item.strip() for item in items if item.strip()]
    return [f"- {item}" for item in values] if values else [empty]


def format_memo(
    brief: ResearchBrief,
    topic: str,
    selected_assumptions: Sequence[dict[str, Any]],
    canon_matches: Sequence[CanonMatch],
    run_date: date,
    model: str,
    mock: bool,
    native_citation_urls: set[str] | None = None,
) -> str:
    assumption_by_id = {item["id"]: item for item in selected_assumptions}
    native_citation_urls = native_citation_urls or set()
    tags = ["research", "pending-review", brief.lane]
    report_id = f"research_{run_date.isoformat()}_{slugify(topic)[:48]}"
    lines = [
        f"# {brief.title}",
        f"Tags: {', '.join(f'[{tag}]' for tag in tags)}",
        "",
        "> **Status:** Non-canonical research draft pending human review.",
        f"> **Mode:** {'MOCK - synthetic test data' if mock else 'LIVE web research'}",
        f"> **Generated:** {run_date.isoformat()}",
        f"> **Model:** {model if not mock else 'none'}",
        "",
        "## Research Question",
        "",
        topic,
        "",
        "## Executive Summary",
        "",
        brief.executive_summary,
        "",
        "## Research Scope",
        "",
        f"- Lane: `{brief.lane}`",
        f"- Research window: {brief.research_window}",
        "- Tracked assumptions: "
        + ", ".join(f"`{item['id']}`" for item in selected_assumptions),
        "",
        "## Observed Developments",
        "",
    ]
    for development in brief.developments:
        citations = ", ".join(f"`{source_id}`" for source_id in development.source_ids)
        lines.extend(
            [
                f"### {development.title}",
                "",
                f"- Event date: {development.event_date}",
                f"- Sources: {citations or 'None'}",
                f"- Observed fact: {development.observed_fact}",
                f"- Significance: {development.significance}",
                "",
            ]
        )

    lines.extend(["## Assumption Assessments", ""])
    for assessment in brief.assumption_assessments:
        assumption = assumption_by_id.get(assessment.assumption_id, {})
        title = assumption.get("title", "Unknown assumption")
        citations = ", ".join(f"`{source_id}`" for source_id in assessment.source_ids)
        lines.extend(
            [
                f"### {assessment.assumption_id}: {title}",
                "",
                f"- Proposed verdict: **{assessment.verdict}**",
                f"- Confidence: **{assessment.confidence}**",
                f"- Sources: {citations or 'None'}",
                f"- Evidence: {assessment.evidence_summary}",
                f"- Real-world implication: {assessment.real_world_implication}",
                f"- PostSingularity implication: {assessment.post_singularity_implication}",
                "",
            ]
        )

    lines.extend(["## Canon Implementation Plan", ""])
    if brief.canon_implications:
        for implication in brief.canon_implications:
            assumptions = ", ".join(
                f"`{assumption_id}`" for assumption_id in implication.assumption_ids
            )
            citations = ", ".join(
                f"`{source_id}`" for source_id in implication.source_ids
            )
            lines.extend(
                [
                    f"### `{implication.path}` -> {implication.target_heading}",
                    "",
                    f"- Priority: **{implication.priority}**",
                    f"- Recommendation: **{implication.recommendation}**",
                    f"- Evidence relationship: **{implication.relationship}**",
                    f"- Assumptions: {assumptions or 'None'}",
                    f"- Sources: {citations or 'None'}",
                    f"- Why this location: {implication.rationale}",
                    f"- Proposed change: {implication.proposed_change}",
                    "- Implementation steps:",
                    *[
                        f"  {index}. {step}"
                        for index, step in enumerate(
                            implication.implementation_steps, start=1
                        )
                    ],
                    "- Dependencies or conflicts:",
                    *(
                        [
                            f"  - {item}"
                            for item in implication.dependencies_or_conflicts
                        ]
                        or ["  - None identified."]
                    ),
                    "",
                ]
            )
    else:
        lines.extend(["No canon changes are recommended.", ""])

    lines.extend(["### Nearby Canon Used for Context", ""])
    if canon_matches:
        for match in canon_matches:
            lines.append(f"- [`{match.path}`](../../{match.path}) — {match.reason}")
    else:
        lines.append("- No nearby canon files were selected.")

    lines.extend(["", "## Uncertainties", ""])
    lines.extend(_bullets(brief.uncertainties))
    lines.extend(["", "## Watchlist", ""])
    lines.extend(_bullets(brief.watchlist))
    lines.extend(["", "## Sources", ""])
    for source in brief.sources:
        url = str(source.url)
        annotation = (
            "native citation verified"
            if url in native_citation_urls
            else "URL supplied in structured research output"
        )
        lines.append(
            f"- `{source.id}` [{source.title}]({url}) — {source.publisher}; "
            f"{source.published_at}; {source.source_type}; {annotation}. "
            f"{source.why_relevant}"
        )

    lines.extend(
        [
            "",
            "## Human Review Checklist",
            "",
            "- [ ] Open every source and verify the cited claim and date.",
            "- [ ] Confirm demonstrations are not described as deployments.",
            "- [ ] Check for contradictory evidence and missing primary sources.",
            "- [ ] Accept, revise, or reject each proposed assumption verdict.",
            "- [ ] Verify every target file and heading still exists.",
            "- [ ] Accept, revise, or reject each proposed repository edit.",
            "- [ ] Move accepted changes through the normal contribution workflow.",
            "",
            "```json",
            json.dumps(
                {
                    "id": report_id,
                    "type": "research_brief",
                    "name": brief.title,
                    "tags": tags,
                    "introduced_in_cycle": 0,
                    "related_characters": [],
                    "impact": ["assumption tracking", "canon review"],
                    "tracked_assumptions": [
                        item["id"] for item in selected_assumptions
                    ],
                    "generated_by": "postsingularity-research",
                    "mock": mock,
                },
                indent=2,
            ),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def write_memo(
    markdown: str,
    topic: str,
    lane: str,
    output_dir: Path,
    run_date: date,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{run_date.isoformat()}-{lane}-{slugify(topic)[:64]}"
    path = output_dir / f"{stem}.md"
    suffix = 2
    while path.exists():
        path = output_dir / f"{stem}-{suffix}.md"
        suffix += 1
    path.write_text(markdown, encoding="utf-8")
    return path


def append_submission_log(
    submissions_log: Path,
    report_path: Path,
    topic: str,
    repo_root: Path = REPO_ROOT,
) -> bool:
    text = submissions_log.read_text(encoding="utf-8")
    try:
        relative_path = report_path.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        relative_path = report_path.as_posix()
    if relative_path in text:
        return False
    row = (
        f"| 0 | research agent | [{report_path.name}]({relative_path}) | pending | "
        f"{topic.replace('|', '/')} |"
    )
    lines = text.splitlines()
    table_indices = [
        index for index, line in enumerate(lines) if line.lstrip().startswith("|")
    ]
    if not table_indices:
        raise ValueError(f"Could not find a table to append to in {submissions_log}")
    lines.insert(table_indices[-1] + 1, row)
    new_text = "\n".join(lines)
    if text.endswith("\n"):
        new_text += "\n"
    submissions_log.write_text(new_text, encoding="utf-8")
    return True


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Research real-world developments and map them to PostSingularity "
            "assumptions without changing canon."
        )
    )
    parser.add_argument("--topic", help="Research question or topic; omitted uses weekly rotation")
    parser.add_argument(
        "--lane",
        choices=["auto", *LANES.keys()],
        default="auto",
        help="Research lane; defaults to inference or weekly rotation",
    )
    parser.add_argument(
        "--assumption",
        action="append",
        default=[],
        metavar="ID",
        help="Restrict the run to an assumption ID; may be repeated",
    )
    parser.add_argument("--lookback-days", type=int, default=30)
    parser.add_argument("--model", default=os.environ.get("OPENAI_MODEL", DEFAULT_MODEL))
    parser.add_argument(
        "--reasoning-effort",
        choices=["none", "low", "medium", "high", "xhigh", "max"],
        default="medium",
    )
    parser.add_argument("--mock", action="store_true", help="Use deterministic synthetic data")
    parser.add_argument("--dry-run", action="store_true", help="Print instead of writing files")
    parser.add_argument("--no-log", action="store_true", help="Do not update submissions-log.md")
    parser.add_argument("--list-assumptions", action="store_true")
    parser.add_argument("--assumptions-file", type=Path, default=DEFAULT_ASSUMPTIONS_PATH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--submissions-log", type=Path, default=DEFAULT_SUBMISSIONS_LOG)
    return parser


@dataclass(frozen=True)
class ResearchRun:
    """Everything a research backend needs for one CLI invocation."""

    topic: str
    lane: str
    lookback_days: int
    assumptions: list[dict[str, Any]]
    canon_matches: list[CanonMatch]
    run_date: date


def prepare_research_run(
    args: argparse.Namespace,
    assumptions: Sequence[dict[str, Any]],
    run_date: date,
) -> ResearchRun:
    """Resolve the topic, lane, tracked assumptions, and canon context."""
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
    canon_matches = select_canon_context(
        topic,
        lane,
        load_canon_files(),
        selected,
    )
    return ResearchRun(
        topic=topic,
        lane=lane,
        lookback_days=args.lookback_days,
        assumptions=list(selected),
        canon_matches=list(canon_matches),
        run_date=run_date,
    )


def run_research_cli(
    args: argparse.Namespace,
    live_runner: Callable[[ResearchRun], tuple[ResearchBrief, set[str]]],
    model_label: str,
    error_label: str,
) -> int:
    """Run the shared assumption research pipeline around a research backend."""
    try:
        assumptions = load_assumptions(args.assumptions_file)
        if args.list_assumptions:
            for item in assumptions:
                print(f"{item['id']}\t{item['lane']}\t{item['status']}\t{item['title']}")
            return 0

        run = prepare_research_run(args, assumptions, datetime.now(timezone.utc).date())

        if args.mock:
            brief = build_mock_brief(
                run.topic,
                run.lane,
                run.assumptions,
                run.canon_matches,
                run.run_date,
                run.lookback_days,
            )
            validate_brief(brief, run.assumptions, run.canon_matches)
            native_citations: set[str] = set()
        else:
            brief, native_citations = live_runner(run)

        markdown = format_memo(
            brief,
            run.topic,
            run.assumptions,
            run.canon_matches,
            run.run_date,
            model_label,
            args.mock,
            native_citations,
        )
        if args.dry_run:
            print(markdown)
            return 0

        report_path = write_memo(
            markdown, run.topic, run.lane, args.output_dir, run.run_date
        )
        if not args.no_log:
            append_submission_log(args.submissions_log, report_path, run.topic)
        print(report_path)
        return 0
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"{error_label}: {exc}", file=sys.stderr)
        return 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.lookback_days < 1:
        parser.error("--lookback-days must be at least 1")

    def live_runner(run: ResearchRun) -> tuple[ResearchBrief, set[str]]:
        return run_live_research(
            run.topic,
            run.lane,
            run.lookback_days,
            run.assumptions,
            run.canon_matches,
            run.run_date,
            args.model,
            args.reasoning_effort,
        )

    return run_research_cli(args, live_runner, args.model, "research agent error")


if __name__ == "__main__":
    raise SystemExit(main())

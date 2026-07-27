# Daily Research Crew
Tags: [research], [agents], [workflow]

## Summary

The daily research crew is a controlled CrewAI pipeline that watches current AI
and technology developments, tests them against the assumptions registry, and
creates non-canonical briefs for human review.

GitHub Actions starts one run each day. The crew is not a persistent background
process: it starts, completes six bounded tasks, writes a review artifact, opens
a pull request, and exits.

## Crew Roles

1. **Signal Scout** searches for recent primary and authoritative evidence.
2. **Counterevidence Scout** searches for limitations, failed replications, and
   deployment barriers.
3. **Evidence Auditor** deduplicates sources, reconciles conflicts, and removes
   unsupported claims.
4. **Assumption Analyst** assesses every selected assumption and maps the
   real-world and storyworld implications.
5. **Repository Implementation Mapper** guarantees declared assumption files are
   considered, then identifies exact files, existing heading anchors, evidence,
   proposed edits, implementation steps, priorities, and canon conflicts.
6. **Canon Review Editor** assembles a structured brief without changing canon.

The process is sequential and uses typed task outputs. Deterministic Python
validation rejects unknown repository paths, invented headings, unselected
assumptions, and unknown source IDs before any file is written.

## Running Locally

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-research-crew.txt -e .
$env:OPENAI_API_KEY = "your key"
.\.venv\Scripts\python.exe -m tools.research_crew --lane ai
```

Use `--topic` for a specific question. When no topic is supplied, the crew
rotates through the eight research lanes. Use `--mock --dry-run` to verify
selection and formatting without CrewAI calls or API spend.

## Review Boundary

Crew outputs always go to
[`pending-review/agent-research/`](../pending-review/agent-research/). The crew
may recommend strengthening, weakening, contradicting, debating, or monitoring
an assumption. Its implementation plan is a proposal for human review; it does
not update the registry or canon.

```json
{
  "id": "meta_daily_research_crew",
  "type": "meta",
  "name": "Daily Research Crew",
  "tags": ["research", "agents", "workflow"],
  "introduced_in_cycle": 0,
  "related_characters": [],
  "impact": ["daily evidence review", "assumption tracking"]
}
```

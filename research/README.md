# Research and Assumption Tracking
Tags: [research], [assumptions], [forecasting]

## Summary

This directory defines the real-world assumptions and predictions that the
PostSingularity research agent watches. The machine-readable source of truth is
[`assumptions.json`](./assumptions.json).

The registry does not declare that a storyworld premise is true. It gives each
premise a stable identifier, names the relevant canon, and records the signals
that would strengthen or weaken it. Research reports may recommend a status
change, but only a human reviewer updates the registry or canon.

## Workflow

1. Select an assumption, research lane, or open topic.
2. Run the six-role daily crew with `postsingularity-crew`, or use
   `postsingularity-research` for a focused single-agent pass.
3. Review the generated brief in
   [`pending-review/agent-research/`](../pending-review/agent-research/).
4. Verify every source and distinguish observed evidence from inference.
5. Decide whether to update an assumption, debate a canon change, or simply
   keep watching.

See [`CREW.md`](./CREW.md) for the crew roles, local commands, daily schedule,
and human-review boundary.

## Registry Statuses

- `unassessed`: no reviewed real-world evidence has been recorded.
- `strengthened`: reviewed evidence makes the premise more plausible.
- `weakened`: reviewed evidence makes the premise less plausible.
- `contradicted`: reviewed evidence conflicts materially with the premise.
- `mixed`: reviewed evidence points in more than one direction.
- `retired`: the premise is no longer actively tracked.

```json
{
  "id": "meta_research_tracking",
  "type": "meta",
  "name": "Research and Assumption Tracking",
  "tags": ["research", "assumptions", "forecasting"],
  "introduced_in_cycle": 0,
  "related_characters": [],
  "impact": ["evidence tracking", "canon review"]
}
```

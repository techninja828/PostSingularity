# Issue Resolution Workflow
Tags: [meta], [workflow], [contribution]

## Summary
This guide outlines the full lifecycle of a contribution, from initial submission to final merge.

## Lifecycle
1. **Initial Submission** – Place new or uncertain ideas in `pending-review/`.
2. **Logging** – Record each submission in `submissions-log.md` with notes and intended cycle.
3. **Discussion** – If debate is needed, create a debate branch and linked issue following [debate-branches.md](debate-branches.md).
4. **Validation** – Run `python tools/scripts/validate_metadata.py` and other checks to ensure metadata and structure.
5. **Approval** – Maintainers review discussion outcomes and validation results, making revisions as needed.
6. **Final Merge** – Approved work moves to its destination or is removed if rejected, and the log is updated.

## Cultural Effects
Clear resolution steps keep the world coherent while welcoming experimentation.

## Philosophical Tensions
Does structured process fuel creativity or constrain it?

## Story Use
Apply this workflow when contributing lore, characters, or systems to the Post Singularity universe.

```json
{
  "id": "meta_issue_resolution",
  "type": "meta",
  "name": "Issue Resolution Workflow",
  "tags": ["workflow", "contribution"],
  "introduced_in_cycle": 0,
  "related_characters": [],
  "impact": ["consistent contributions"]
}
```

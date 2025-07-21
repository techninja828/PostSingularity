# Debate Branches Guide
Tags: [meta], [workflow], [collaboration]

## Summary
Use a debate branch when a contribution might significantly alter existing lore or cause disagreement. This process keeps discussions organized and transparent.

## Procedure
1. Create a branch named `debate/your-topic` from `main`.
2. Open a GitHub issue with the **Debate Branch** template and link the branch.
3. Describe the problem and proposed changes in the issue, referencing relevant files.
4. Discuss in the issue thread while committing updates to the branch.
5. *Optional:* call for a vote by posting a `### Vote` comment that lists the options. Participants respond with `:+1:` or `-1:` reactions (or `+1`/`-1` comments). A proposal passes with a simple majority or a 60% threshold as agreed by the maintainers.
6. When consensus or a vote resolves the matter, post a `### Resolution` comment summarizing the decision and reference the final commit.
7. Merge or close the branch and log the outcome in [`../submissions-log.md`](../submissions-log.md).

## Comment Structure
- **Argument**: State your position succinctly, referencing line numbers or commits.
- **Counterargument**: Address the prior argument or provide new evidence.
- Keep each comment focused on a single idea so others can reply clearly.

## Voting
When discussion stalls or multiple proposals remain, maintainers may call for a vote. Summarize the options in a `### Vote` comment. Participants express support with `:+1:` reactions or `+1` comments. Tally the responses and note the threshold used (simple majority or 60%). Record the outcome in the issue before posting the final resolution.

## Cultural Effects
Structured debates encourage thoughtful collaboration without stalling other work.

## Philosophical Tensions
Does formal debate help refine ideas, or can it stifle spontaneity?

## Story Use
Apply this method when introducing technology, characters, or lore that might conflict with prior contributions.

```json
{
  "id": "meta_debate_branches",
  "type": "meta",
  "name": "Debate Branches Guide",
  "tags": ["workflow", "collaboration"],
  "introduced_in_cycle": 0,
  "related_characters": [],
  "impact": ["structured debate"]
}
```

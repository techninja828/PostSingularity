# Episode Pipeline – From Lore to Screen
Tags: [integration], [pipeline], [episodes], [ai]

## Summary
The episode pipeline converts repository lore into scripts or storyboards for live or animated episodes. Markdown files provide structured lore while metadata keeps track of continuity.

## Function
1. Writers add or update Markdown files across the project, ensuring each contains a `Tags:` line and a JSON metadata block.
2. A custom export script parses these files, collecting summaries, functions, and metadata into a unified JSON dataset.
3. This dataset feeds into an AI model that drafts dialogue, scene descriptions, and camera cues based on relevant characters, locations, and technologies.
4. Editors review the AI output, updating the lore if new details become canonical.

## Required Data Exports
- **Metadata Validation:** Run `scripts/validate_metadata.py` to verify that all Markdown files include tags and JSON blocks.
- **Data Export:** Use a preprocessing tool to convert Markdown and metadata into structured JSON. Each entry should reference character IDs, location IDs, and thematic tags so the AI can retrieve context quickly.

## Preprocessing Steps
1. Strip Markdown formatting not needed by the model (such as index lists).
2. Merge data into per-episode bundles, grouping relevant lore by tag or cycle number.
3. Provide the AI model with the cleaned JSON dataset to generate scene outlines or fully realized scripts.

```json
{
  "id": "integration_episode_pipeline",
  "type": "protocol",
  "name": "Episode Pipeline",
  "tags": ["integration", "pipeline", "episodes", "ai"],
  "introduced_in_cycle": 0,
  "related_characters": [],
  "impact": ["story generation", "production workflow"]
}
```

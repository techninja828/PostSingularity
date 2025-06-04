# Scripts
Tags: [meta], [scripts]

This directory collects small utilities for working with the repository.

## `validate_metadata.py`

Scan markdown files to ensure they contain either a `tags:` line or a JSON block. The script exits with a non-zero status if any files are missing these metadata hints.

```bash
python validate_metadata.py [path]
```

If no path is provided, the current directory is scanned recursively.

```json
{
  "id": "scripts_overview",
  "type": "reference",
  "name": "Scripts Directory",
  "tags": ["scripts"],
  "introduced_in_cycle": 0,
  "related_characters": [],
  "impact": ["utilities"]
}
```

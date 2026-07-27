#!/usr/bin/env python3
"""Validate metadata in Markdown files.

Usage:
    python validate_metadata.py [path]

The script recursively scans `.md` files under the given path (current
working directory by default). Each file must contain **both** a line
starting with ``Tags:`` and a fenced code block beginning with
````json```. JSON metadata blocks must use standard fenced code syntax:

```json
{ ... }
```

Any file missing either requirement will be listed and the program exits with
status 1.
"""

import sys
from pathlib import Path

if __package__ in (None, ""):  # direct execution: python tools/scripts/validate_metadata.py
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.markdown_utils import (
    EXCLUDED_DIRS,
    collect_markdown_files,
    has_json_block,
    has_tag_line,
    read_text,
)

__all__ = [
    "EXCLUDED_DIRS",
    "collect_markdown_files",
    "has_required_metadata",
    "check_file",
    "main",
]


def has_required_metadata(text: str) -> bool:
    """Return True if text contains both a Tags line and a JSON block."""
    return has_tag_line(text) and has_json_block(text)


def check_file(path: str) -> bool:
    content = read_text(path)
    if content is None:
        print(f"Error reading {path}")
        return False
    return has_required_metadata(content)


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    md_files = collect_markdown_files(root)

    missing = [f for f in md_files if not check_file(f)]

    if missing:
        print("Files missing required Tags line and JSON metadata block:")
        for f in missing:
            print(f"- {f}")
        sys.exit(1)
    else:
        print("All markdown files contain both Tags line and JSON metadata block.")


if __name__ == '__main__':
    main()

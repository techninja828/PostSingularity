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

import os
import re
import sys
from typing import List

TAG_REGEX = re.compile(r'^tags\s*:', re.IGNORECASE | re.MULTILINE)
JSON_BLOCK_REGEX = re.compile(r'```json', re.IGNORECASE)
EXCLUDED_DIRS = {'.git', '.venv', '.pytest_cache', '__pycache__', 'node_modules'}


def has_required_metadata(text: str) -> bool:
    """Return True if text contains both a Tags line and a JSON block."""
    return bool(TAG_REGEX.search(text)) and bool(JSON_BLOCK_REGEX.search(text))


class MetadataCheckError(Exception):
    """Raised when a file cannot be read for metadata validation."""


def check_file(path: str) -> bool:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except OSError as e:
        raise MetadataCheckError(f"Error reading {path}: {e}") from e
    return has_required_metadata(content)


def collect_markdown_files(root: str) -> List[str]:
    result = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [name for name in dirnames if name not in EXCLUDED_DIRS]
        for filename in filenames:
            if filename.lower().endswith('.md'):
                result.append(os.path.join(dirpath, filename))
    return result


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    md_files = collect_markdown_files(root)

    missing = []
    errors = []
    for f in md_files:
        try:
            if not check_file(f):
                missing.append(f)
        except MetadataCheckError as exc:
            errors.append(str(exc))

    for message in errors:
        print(message, file=sys.stderr)

    if missing:
        print("Files missing required Tags line and JSON metadata block:")
        for f in missing:
            print(f"- {f}")

    if missing or errors:
        sys.exit(1)

    print("All markdown files contain both Tags line and JSON metadata block.")


if __name__ == '__main__':
    main()

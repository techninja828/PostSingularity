#!/usr/bin/env python3
"""Validate metadata in Markdown files.

Usage:
    python validate_metadata.py [path]

The script recursively scans `.md` files under the given path (current
working directory by default). Each file must contain either a line
starting with ``tags:`` or a fenced code block beginning with
````json```. Any file missing both will be listed and the program exits
with status 1.
"""

import os
import re
import sys
from typing import List

TAG_REGEX = re.compile(r'^tags\s*:', re.IGNORECASE | re.MULTILINE)
JSON_BLOCK_REGEX = re.compile(r'```json', re.IGNORECASE)


def has_required_metadata(text: str) -> bool:
    return bool(TAG_REGEX.search(text) or JSON_BLOCK_REGEX.search(text))


def check_file(path: str) -> bool:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        return has_required_metadata(content)
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return False


def collect_markdown_files(root: str) -> List[str]:
    result = []
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.lower().endswith('.md'):
                result.append(os.path.join(dirpath, filename))
    return result


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    md_files = collect_markdown_files(root)

    missing = [f for f in md_files if not check_file(f)]

    if missing:
        print("Files missing metadata:")
        for f in missing:
            print(f"- {f}")
        sys.exit(1)
    else:
        print("All markdown files contain required metadata.")


if __name__ == '__main__':
    main()

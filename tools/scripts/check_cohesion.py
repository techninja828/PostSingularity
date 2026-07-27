#!/usr/bin/env python3
"""Check cross-references in JSON metadata across Markdown files.

This script parses every `.md` file under the provided root (current
working directory by default) and extracts JSON metadata blocks. It then
verifies two types of references:

1. Each value in `related_characters` must correspond to a Markdown file
   under the `characters/` directory.
2. Each `introduced_in_cycle` value must appear in
   `worldbible/timeline.md` as a referenced cycle.

At the end a "cohesiveness score" is printed representing the
percentage of references that successfully resolve.

Usage:
    python tools/scripts/check_cohesion.py [root]
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List

if __package__ in (None, ""):  # direct execution: python tools/scripts/check_cohesion.py
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.markdown_utils import (
    EXCLUDED_DIRS,
    collect_markdown_files,
    extract_json_blocks,
    read_text,
)

CYCLE_REGEX = re.compile(r"cycle\s*(\d+)", re.IGNORECASE)

__all__ = ["EXCLUDED_DIRS", "collect_markdown_files", "extract_metadata", "load_cycles", "main"]


def extract_metadata(path: str) -> List[Dict]:
    try:
        text = read_text(path)
    except OSError as exc:
        print(f"Warning: could not read {path}: {exc}", file=sys.stderr)
        return []
    return extract_json_blocks(text, source=path)


def load_cycles(timeline_path: str) -> List[int]:
    try:
        text = read_text(timeline_path)
    except OSError as exc:
        print(
            f"Warning: could not read timeline {timeline_path}: {exc}",
            file=sys.stderr,
        )
        return []
    return [int(m) for m in CYCLE_REGEX.findall(text)]


def main() -> None:
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    md_files = collect_markdown_files(root)

    characters_dir = os.path.join(root, "characters")
    try:
        char_entries = os.listdir(characters_dir)
    except OSError as exc:
        print(f"Error: could not list characters directory {characters_dir}: {exc}", file=sys.stderr)
        sys.exit(1)
    char_files = {os.path.splitext(f)[0].lower() for f in char_entries if f.endswith(".md")}

    cycles = load_cycles(os.path.join(root, "worldbible", "timeline.md"))

    unresolved_chars = []
    unresolved_cycles = []

    total_refs = 0
    resolved_refs = 0

    for path in md_files:
        for meta in extract_metadata(path):
            # related_characters check
            rc = meta.get("related_characters", [])
            for name in rc:
                total_refs += 1
                if name.lower() in char_files:
                    resolved_refs += 1
                else:
                    unresolved_chars.append((path, name))

            # introduced_in_cycle check
            if "introduced_in_cycle" in meta:
                total_refs += 1
                cycle = meta["introduced_in_cycle"]
                if isinstance(cycle, int) and cycle in cycles:
                    resolved_refs += 1
                else:
                    unresolved_cycles.append((path, cycle))

    # print results
    if unresolved_chars:
        print("Missing character references:")
        for path, name in unresolved_chars:
            print(f"  {path}: {name}")

    if unresolved_cycles:
        print("Items with cycles not found in timeline:")
        for path, cycle in unresolved_cycles:
            print(f"  {path}: cycle {cycle}")

    if total_refs:
        score = resolved_refs / total_refs * 100
    else:
        score = 100.0
    print(f"Cohesiveness score: {score:.2f}% ({resolved_refs}/{total_refs} references)")


if __name__ == "__main__":
    main()

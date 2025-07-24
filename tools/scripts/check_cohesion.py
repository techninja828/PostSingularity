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

import json
import os
import re
import sys
from typing import List, Dict

JSON_BLOCK = re.compile(r"```json\s*(\{.*?\})\s*```", re.DOTALL | re.IGNORECASE)
CYCLE_REGEX = re.compile(r"cycle\s*(\d+)", re.IGNORECASE)


def collect_markdown_files(root: str) -> List[str]:
    files = []
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            if name.lower().endswith(".md"):
                files.append(os.path.join(dirpath, name))
    return files


def extract_metadata(path: str) -> List[Dict]:
    try:
        text = open(path, "r", encoding="utf-8").read()
    except Exception:
        return []
    blocks = JSON_BLOCK.findall(text)
    metadata = []
    for block in blocks:
        try:
            metadata.append(json.loads(block))
        except json.JSONDecodeError:
            pass
    return metadata


def load_cycles(timeline_path: str) -> List[int]:
    try:
        text = open(timeline_path, "r", encoding="utf-8").read()
    except Exception:
        return []
    return [int(m) for m in CYCLE_REGEX.findall(text)]


def main() -> None:
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    md_files = collect_markdown_files(root)

    characters_dir = os.path.join(root, "characters")
    char_files = {os.path.splitext(f)[0].lower() for f in os.listdir(characters_dir) if f.endswith(".md")}

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

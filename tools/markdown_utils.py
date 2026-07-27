"""Shared helpers for locating and parsing repository Markdown files."""

from __future__ import annotations

import json
import os
import re
import sys
from typing import Any

EXCLUDED_DIRS = {".git", ".venv", ".pytest_cache", "__pycache__", "node_modules"}

TAG_LINE_RE = re.compile(r"^tags\s*:\s*(.+)$", re.IGNORECASE | re.MULTILINE)
TAG_VALUE_RE = re.compile(r"\[([^\]]+)\]")
JSON_BLOCK_RE = re.compile(r"```json\s*(\{.*?\})\s*```", re.DOTALL | re.IGNORECASE)
JSON_FENCE_RE = re.compile(r"```json", re.IGNORECASE)
TITLE_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)


def collect_markdown_files(root: str) -> list[str]:
    """Return every Markdown file under ``root``, skipping generated directories."""
    files: list[str] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [name for name in dirnames if name not in EXCLUDED_DIRS]
        for name in filenames:
            if name.lower().endswith(".md"):
                files.append(os.path.join(dirpath, name))
    return files


def read_text(path: str) -> str:
    """Return the file's contents; raises OSError when it cannot be read."""
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def has_tag_line(text: str) -> bool:
    return bool(TAG_LINE_RE.search(text))


def has_json_block(text: str) -> bool:
    return bool(JSON_FENCE_RE.search(text))


def parse_tags(text: str) -> tuple[str, ...]:
    """Extract a Markdown ``Tags: [a], [b]`` line."""
    match = TAG_LINE_RE.search(text)
    if not match:
        return ()
    return tuple(tag.strip().lower() for tag in TAG_VALUE_RE.findall(match.group(1)))


def extract_json_blocks(text: str, source: str | None = None) -> list[dict[str, Any]]:
    """Return every parseable ```json metadata block, warning about the rest."""
    blocks: list[dict[str, Any]] = []
    for raw in JSON_BLOCK_RE.findall(text):
        try:
            blocks.append(json.loads(raw))
        except json.JSONDecodeError as exc:
            if source is not None:
                print(
                    f"Warning: skipping malformed JSON metadata block in {source}: {exc}",
                    file=sys.stderr,
                )
    return blocks


def first_json_block(text: str, source: str | None = None) -> dict[str, Any] | None:
    """Return the first ```json metadata block, or None when absent or malformed."""
    match = JSON_BLOCK_RE.search(text)
    if not match:
        return None
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        if source is not None:
            print(
                f"Warning: malformed JSON metadata in {source}: {exc}",
                file=sys.stderr,
            )
        return None


def extract_title(text: str, fallback: str) -> str:
    match = TITLE_RE.search(text)
    return match.group(1).strip() if match else fallback


def extract_headings(text: str) -> tuple[str, ...]:
    """Return Markdown headings without their leading hash marks."""
    return tuple(match.group(1).strip() for match in HEADING_RE.finditer(text))

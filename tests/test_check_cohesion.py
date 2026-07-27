from pathlib import Path

import pytest

from tools.scripts import check_cohesion


def test_extract_metadata_parses_valid_blocks_and_skips_invalid(tmp_path: Path) -> None:
    md = tmp_path / "doc.md"
    md.write_text(
        "```json\n{\"id\": \"a\"}\n```\n"
        "```json\n{bad json}\n```\n"
        "```json\n{\"id\": \"b\"}\n```\n",
        encoding="utf-8",
    )
    assert check_cohesion.extract_metadata(str(md)) == [{"id": "a"}, {"id": "b"}]


def test_extract_metadata_missing_file_returns_empty() -> None:
    assert check_cohesion.extract_metadata("does-not-exist.md") == []


def test_load_cycles_reads_cycle_numbers(tmp_path: Path) -> None:
    timeline = tmp_path / "timeline.md"
    timeline.write_text("Cycle 0 begins. Later in cycle 3 and CYCLE 12.\n", encoding="utf-8")
    assert check_cohesion.load_cycles(str(timeline)) == [0, 3, 12]


def test_load_cycles_missing_file_returns_empty() -> None:
    assert check_cohesion.load_cycles("nope.md") == []


def _build_repo(tmp_path: Path) -> None:
    characters = tmp_path / "characters"
    characters.mkdir()
    (characters / "aria.md").write_text("# Aria\n", encoding="utf-8")

    worldbible = tmp_path / "worldbible"
    worldbible.mkdir()
    (worldbible / "timeline.md").write_text("Cycle 0 and cycle 1.\n", encoding="utf-8")


def test_main_reports_full_cohesion(tmp_path: Path, monkeypatch, capsys) -> None:
    _build_repo(tmp_path)
    (tmp_path / "story.md").write_text(
        "```json\n{\"related_characters\": [\"Aria\"], \"introduced_in_cycle\": 1}\n```\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(check_cohesion.sys, "argv", ["check_cohesion.py", str(tmp_path)])
    check_cohesion.main()

    out = capsys.readouterr().out
    assert "Cohesiveness score: 100.00% (2/2 references)" in out
    assert "Missing character references" not in out


def test_main_flags_unresolved_references(tmp_path: Path, monkeypatch, capsys) -> None:
    _build_repo(tmp_path)
    (tmp_path / "story.md").write_text(
        "```json\n{\"related_characters\": [\"Ghost\"], \"introduced_in_cycle\": 99}\n```\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(check_cohesion.sys, "argv", ["check_cohesion.py", str(tmp_path)])
    check_cohesion.main()

    out = capsys.readouterr().out
    assert "Missing character references:" in out
    assert "Ghost" in out
    assert "Items with cycles not found in timeline:" in out
    assert "cycle 99" in out
    assert "Cohesiveness score: 0.00% (0/2 references)" in out


def test_main_defaults_score_to_full_without_references(tmp_path: Path, monkeypatch, capsys) -> None:
    _build_repo(tmp_path)
    (tmp_path / "plain.md").write_text("# No metadata here\n", encoding="utf-8")
    monkeypatch.setattr(check_cohesion.sys, "argv", ["check_cohesion.py", str(tmp_path)])
    check_cohesion.main()

    out = capsys.readouterr().out
    assert "Cohesiveness score: 100.00% (0/0 references)" in out

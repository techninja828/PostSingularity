from pathlib import Path

import pytest

from tools.scripts import validate_metadata


def test_has_required_metadata_true_when_both_present() -> None:
    text = "Tags: [meta]\n\n```json\n{}\n```\n"
    assert validate_metadata.has_required_metadata(text) is True


def test_has_required_metadata_false_when_missing_tags() -> None:
    assert validate_metadata.has_required_metadata("```json\n{}\n```\n") is False


def test_has_required_metadata_false_when_missing_json_block() -> None:
    assert validate_metadata.has_required_metadata("Tags: [meta]\n") is False


def test_check_file_reads_file(tmp_path: Path) -> None:
    good = tmp_path / "good.md"
    good.write_text("Tags: [x]\n```json\n{}\n```\n", encoding="utf-8")
    bad = tmp_path / "bad.md"
    bad.write_text("no metadata\n", encoding="utf-8")

    assert validate_metadata.check_file(str(good)) is True
    assert validate_metadata.check_file(str(bad)) is False


def test_check_file_handles_unreadable_path(capsys) -> None:
    assert validate_metadata.check_file("missing-file.md") is False
    assert "Error reading" in capsys.readouterr().out


def test_main_succeeds_when_all_files_valid(tmp_path: Path, monkeypatch, capsys) -> None:
    (tmp_path / "doc.md").write_text("Tags: [x]\n```json\n{}\n```\n", encoding="utf-8")
    monkeypatch.setattr(validate_metadata.sys, "argv", ["validate_metadata.py", str(tmp_path)])

    validate_metadata.main()

    assert "All markdown files contain" in capsys.readouterr().out


def test_main_exits_nonzero_when_file_invalid(tmp_path: Path, monkeypatch, capsys) -> None:
    (tmp_path / "doc.md").write_text("Tags: [x]\n```json\n{}\n```\n", encoding="utf-8")
    (tmp_path / "broken.md").write_text("missing metadata\n", encoding="utf-8")
    monkeypatch.setattr(validate_metadata.sys, "argv", ["validate_metadata.py", str(tmp_path)])

    with pytest.raises(SystemExit) as excinfo:
        validate_metadata.main()

    assert excinfo.value.code == 1
    out = capsys.readouterr().out
    assert "Files missing required" in out
    assert "broken.md" in out

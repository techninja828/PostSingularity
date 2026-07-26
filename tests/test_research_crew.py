from pathlib import Path

from tools import research_crew as crew_module
from tools.research_agent import (
    ResearchBrief,
    load_assumptions,
    load_canon_files,
    nearby_canon,
    select_assumptions,
)


def test_crewai_model_name_adds_provider_prefix() -> None:
    assert crew_module.crewai_model_name("gpt-5.6") == "openai/gpt-5.6"
    assert crew_module.crewai_model_name("openai/gpt-5.6") == "openai/gpt-5.6"


def test_intermediate_schemas_are_strict() -> None:
    assert crew_module.EvidencePacket.model_config["extra"] == "forbid"
    assert crew_module.AuditedEvidence.model_config["extra"] == "forbid"
    assert crew_module.AnalysisPacket.model_config["extra"] == "forbid"


def test_mock_crew_cli_uses_existing_pipeline(capsys) -> None:
    result = crew_module.main(
        [
            "--topic",
            "persistent AI agent memory",
            "--lane",
            "ai",
            "--mock",
            "--dry-run",
        ]
    )
    assert result == 0
    output = capsys.readouterr().out
    assert "MOCK - synthetic test data" in output
    assert "Non-canonical research draft" in output


def test_build_research_crew_has_five_bounded_roles(monkeypatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "test-only-not-a-real-key")
    monkeypatch.setenv("OTEL_SDK_DISABLED", "true")
    topic = "AI agents and persistent memory"
    assumptions = load_assumptions()
    selected = select_assumptions(topic, "ai", assumptions)
    matches = nearby_canon(topic, "ai", load_canon_files())

    crew, final_task = crew_module.build_research_crew(
        topic,
        "ai",
        7,
        selected,
        matches,
        verbose=False,
    )

    assert len(crew.agents) == 5
    assert len(crew.tasks) == 5
    assert final_task.output_pydantic is ResearchBrief
    assert all(agent.allow_delegation is False for agent in crew.agents)


def test_github_workflow_runs_daily() -> None:
    workflow = (
        Path(__file__).parents[1] / ".github" / "workflows" / "research-agent.yml"
    ).read_text(encoding="utf-8")
    assert 'cron: "0 16 * * *"' in workflow
    assert "tools.research_crew" in workflow
    assert "requirements-research-crew.txt" in workflow
    assert "OPENAI_API_KEY is not configured" in workflow

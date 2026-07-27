import pytest

from tools.chatbot import app as chatbot


@pytest.fixture
def sample_repo(monkeypatch):
    texts = {
        "worldbible/overview.md": "post singularity begins on day zero when agi arrives.",
        "characters/aria.md": "aria is an emotional intelligence guide.",
    }
    monkeypatch.setattr(chatbot, "repo_texts", texts)
    return texts


def test_is_relevant_matches_keyword(sample_repo) -> None:
    assert chatbot.is_relevant("tell me about post singularity") is True


def test_is_relevant_matches_repo_token(sample_repo) -> None:
    assert chatbot.is_relevant("who is aria") is True


def test_is_relevant_rejects_offtopic(sample_repo) -> None:
    assert chatbot.is_relevant("qwerty zzz") is False


def test_search_repo_returns_snippet_with_source(sample_repo) -> None:
    result = chatbot.search_repo("aria")
    assert result is not None
    assert result.startswith("From characters/aria.md:")
    assert "aria" in result


def test_search_repo_returns_none_when_no_match(sample_repo) -> None:
    assert chatbot.search_repo("qwerty") is None


def test_index_route_renders_form(sample_repo) -> None:
    client = chatbot.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Post Singularity Chat Bot" in response.data


def test_chat_route_rejects_irrelevant_message(sample_repo) -> None:
    client = chatbot.app.test_client()
    response = client.post("/chat", data={"message": "qwerty zzz"})
    assert response.status_code == 200
    assert b"Please focus on topics related to Post Singularity." in response.data


def test_chat_route_returns_repo_snippet(sample_repo) -> None:
    client = chatbot.app.test_client()
    response = client.post("/chat", data={"message": "aria"})
    assert response.status_code == 200
    assert b"characters/aria.md" in response.data


def test_chat_route_handles_no_repo_match(sample_repo) -> None:
    client = chatbot.app.test_client()
    response = client.post("/chat", data={"message": "ps zzqqxx"})
    assert response.status_code == 200
    assert b"I don&#39;t have information about that" in response.data

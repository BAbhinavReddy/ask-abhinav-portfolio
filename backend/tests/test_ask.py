from fastapi.testclient import TestClient

from backend.app.main import app
from backend.app.api import ask as ask_api


client = TestClient(app)


def test_ask_validation():
    response = client.post(
        "/api/ask",
        json={"question": ""},
    )

    assert response.status_code == 422


def test_ask_success(monkeypatch):
    def mock_retrieve_context(query, top_k=4):
        return [
            "Abhinav works primarily on Python backend development, APIs, and databases.",
            "His backend skills include Python, FastAPI, REST APIs, PostgreSQL, and SQLAlchemy.",
        ]

    def mock_generate_answer(question, context):
        return (
            "Abhinav has experience in Python backend development, "
            "APIs, databases, FastAPI, PostgreSQL, and SQLAlchemy."
        )

    monkeypatch.setattr(
        ask_api,
        "retrieve_context",
        mock_retrieve_context,
    )

    monkeypatch.setattr(
        ask_api,
        "generate_answer",
        mock_generate_answer,
    )

    response = client.post(
        "/api/ask",
        json={
            "question": "What backend experience does Abhinav have?"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "answer" in data

    assert (
        "Python backend development"
        in data["answer"]
    )
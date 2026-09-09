from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_get_profile():
    response = client.get("/api/profile")

    assert response.status_code == 200

    data = response.json()

    assert "name" in data
    assert "title" in data
    assert "summary" in data
    assert "email" in data
    assert "phone" in data
    assert "github" in data
    assert "linkedin" in data
from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_get_skills():
    response = client.get("/api/skills")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    first_skill = data[0]

    assert "id" in first_skill
    assert "name" in first_skill
    assert "category" in first_skill
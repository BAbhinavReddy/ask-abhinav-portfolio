from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_get_experience():
    response = client.get("/api/experience")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    first_experience = data[0]

    assert "id" in first_experience
    assert "company" in first_experience
    assert "role" in first_experience
    assert "location" in first_experience
    assert "start_date" in first_experience
    assert "end_date" in first_experience
    assert "description" in first_experience
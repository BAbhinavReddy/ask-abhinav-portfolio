from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_get_projects():
    response = client.get("/api/projects")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    first_project = data[0]

    assert "id" in first_project
    assert "name" in first_project
    assert "description" in first_project
    assert "github_url" in first_project
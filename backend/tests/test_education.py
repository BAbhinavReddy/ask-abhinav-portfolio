from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_get_education():
    response = client.get("/api/education")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    first_education = data[0]

    assert "id" in first_education
    assert "institution" in first_education
    assert "degree" in first_education
    assert "field_of_study" in first_education
    assert "start_year" in first_education
    assert "end_year" in first_education
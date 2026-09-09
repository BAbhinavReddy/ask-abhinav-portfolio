import requests


BASE_URL = "http://127.0.0.1:8000"


def test_health():
    response = requests.get(f"{BASE_URL}/api/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_profile():
    response = requests.get(f"{BASE_URL}/api/profile")

    assert response.status_code == 200

    data = response.json()

    assert data["name"]
    assert data["title"]


def test_skills():
    response = requests.get(f"{BASE_URL}/api/skills")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_experience():
    response = requests.get(f"{BASE_URL}/api/experience")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_projects():
    response = requests.get(f"{BASE_URL}/api/projects")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_education():
    response = requests.get(f"{BASE_URL}/api/education")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_ask_abhinav():
    response = requests.post(
        f"{BASE_URL}/api/ask",
        json={
            "question": "What Python backend experience does Abhinav have?"
        },
        timeout=60,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["answer"]
    assert isinstance(data["answer"], str)
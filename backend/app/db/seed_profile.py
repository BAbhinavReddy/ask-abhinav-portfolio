from sqlalchemy.orm import Session

from backend.app.db.database import engine
from backend.app.models.profile import Profile


profile_data = {
    "name": "Abhinav Reddy Bobba",
    "title": "Software Engineer",
    "summary": (
        "Software Engineer specializing in Python backend development, "
        "REST APIs, databases, and AI-powered applications."
    ),
    "email": "YOUR_EMAIL",
    "phone": "YOUR_PHONE",
    "github": "YOUR_GITHUB_URL",
    "linkedin": "YOUR_LINKEDIN_URL",
}


with Session(bind=engine) as db:
    profile = Profile(**profile_data)

    db.add(profile)
    db.commit()

    print("Profile inserted successfully.")
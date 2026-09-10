from sqlalchemy.orm import Session

from backend.app.db.database import engine
from backend.app.models.profile import Profile


profile_data = {
    "name": "Abhinav Reddy Bobba",
    "title": "Software Engineer",
    "summary": (
        "Software Engineer specializing in Python backend development, "
        "FastAPI, REST APIs, PostgreSQL, and AI-powered applications, "
        "with hands-on experience building LLM and RAG-based systems."
    ),
    "email": "abfdf@umsystem.edu",
    "phone": "(945) 266-0136",
    "github": "https://github.com/BAbhinavReddy",
    "linkedin": "https://www.linkedin.com/in/abhinav-reddyb/",
}


with Session(bind=engine) as db:
    profile = Profile(**profile_data)

    db.add(profile)
    db.commit()

    print("Profile inserted successfully.")
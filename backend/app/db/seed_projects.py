from sqlalchemy.orm import Session
from sqlalchemy import delete

from backend.app.db.database import engine
from backend.app.models.project import Project


projects = [
    {
        "name": "CareerFlow AI API",
        "description": (
            "AI-powered backend API for tracking job applications, "
            "analyzing job descriptions, and evaluating resume-to-job fit."
        ),
        "github_url": None,
    },
    {
        "name": "Gemini Coding Agent",
        "description": (
            "Autonomous AI coding agent capable of inspecting a codebase, "
            "modifying files, executing Python code, and iteratively debugging "
            "implementation issues."
        ),
        "github_url": None,
    },
    {
        "name": "Ask Abhinav",
        "description": (
            "AI-powered developer portfolio combining a database-driven "
            "single-page website with a recruiter-focused conversational assistant."
        ),
        "github_url": None,
    },
]


with Session(bind=engine) as db:
    db.execute(delete(Project))
    for project_data in projects:
        project = Project(**project_data)
        db.add(project)

    db.commit()

    print(f"Inserted {len(projects)} projects.")
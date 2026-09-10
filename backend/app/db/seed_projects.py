from sqlalchemy.orm import Session
from sqlalchemy import delete

from backend.app.db.database import engine
from backend.app.models.project import Project


projects = [
    {
        "name": "Ask Abhinav — AI Developer Portfolio",
        "description": (
            "AI-powered developer portfolio built with Python, FastAPI, "
            "PostgreSQL, and JavaScript, featuring a recruiter-focused "
            "conversational assistant using LangChain, Google Gemini, "
            "Retrieval-Augmented Generation (RAG), embeddings, and Pinecone "
            "to retrieve portfolio knowledge and generate grounded answers."
        ),
        "github_url": "https://github.com/BAbhinavReddy/ask-abhinav-portfolio",
    },

    {
            "name": "Gemini Coding Agent",
            "description": (
                "AI coding assistant built with Python and Google Gemini that "
                "uses function calling and a modular tool architecture to inspect "
                "files, modify code, execute Python programs, capture execution "
                "results, and iteratively debug implementation issues."
            ),
            "github_url": "https://github.com/BAbhinavReddy/gemini-coding-agent",
        },

    {
        "name": "CareerFlow AI API",
        "description": (
            "Python and FastAPI backend for tracking job applications, "
            "analyzing job descriptions, and evaluating resume-to-job fit. "
            "Uses PostgreSQL, SQLAlchemy, Pydantic, authentication, "
            "LangChain, and Google Gemini to provide AI-powered job analysis "
            "and resume matching."
        ),
        "github_url": "https://github.com/BAbhinavReddy/careerflow-ai-api",
    },

    
]


with Session(bind=engine) as db:
    db.execute(delete(Project))
    for project_data in projects:
        project = Project(**project_data)
        db.add(project)

    db.commit()

    print(f"Inserted {len(projects)} projects.")
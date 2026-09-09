from sqlalchemy.orm import Session
from sqlalchemy import delete

from backend.app.db.database import engine
from backend.app.models.skill import Skill


skills = [
    ("Python", "Languages/Core"),
    ("JavaScript", "Languages/Core"),
    ("SQL", "Languages/Core"),
    ("DSA", "Languages/Core"),
    ("Async Python", "Languages/Core"),
    ("Debugging", "Languages/Core"),

    ("FastAPI", "Backend/APIs"),
    ("REST APIs", "Backend/APIs"),
    ("Pydantic", "Backend/APIs"),
    ("SQLAlchemy", "Backend/APIs"),
    ("JWT/OAuth", "Backend/APIs"),
    ("System Design", "Backend/APIs"),

    ("PostgreSQL", "Databases"),
    ("Vector Search", "Databases"),
    ("Pinecone", "Databases"),

    ("AWS", "Cloud/DevOps"),
    ("Docker", "Cloud/DevOps"),
    ("CI/CD", "Cloud/DevOps"),
    ("GitHub Actions", "Cloud/DevOps"),
    ("Git", "Cloud/DevOps"),
    ("GitHub", "Cloud/DevOps"),
    ("Linux", "Cloud/DevOps"),

    ("pytest", "Testing"),
    ("Postman", "Testing"),

    ("LLMs", "AI/LLM"),
    ("Google Gemini API", "AI/LLM"),
    ("OpenAI API", "AI/LLM"),
    ("LangChain", "AI/LLM"),
    ("RAG", "AI/LLM"),
    ("Embeddings", "AI/LLM"),
    ("Function Calling", "AI/LLM"),
    ("Claude Code", "AI/LLM"),
]


with Session(bind=engine) as db:

    db.execute(delete(Skill))

    for name, category in skills:
        skill = Skill(
            name=name,
            category=category,
        )

        db.add(skill)

    db.commit()

    print(f"Inserted {len(skills)} skills.")
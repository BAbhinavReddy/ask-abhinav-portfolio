from sqlalchemy.orm import Session
from sqlalchemy import delete

from backend.app.db.database import engine
from backend.app.models.skill import Skill


skills = [
    # Languages
    ("Python", "Languages"),
    ("SQL", "Languages"),
    ("JavaScript", "Languages"),
    ("HTML", "Languages"),
    ("CSS", "Languages"),

    # Backend & APIs
    ("FastAPI", "Backend & APIs"),
    ("REST APIs", "Backend & APIs"),
    ("SQLAlchemy (ORM)", "Backend & APIs"),
    ("Pydantic", "Backend & APIs"),
    ("Swagger/OpenAPI", "Backend & APIs"),
    ("System Design", "Backend & APIs"),
    ("Agile", "Backend & APIs"),

    # Databases
    ("PostgreSQL", "Databases"),
    ("Pinecone (vector database)", "Databases"),

    # AI / LLM Engineering
    ("Google Gemini API", "AI / LLM Engineering"),
    ("OpenAI API", "AI / LLM Engineering"),
    ("LangChain", "AI / LLM Engineering"),
    ("Retrieval-Augmented Generation (RAG)", "AI / LLM Engineering"),
    ("Vector Search", "AI / LLM Engineering"),
    ("Embeddings", "AI / LLM Engineering"),
    ("Prompt Engineering", "AI / LLM Engineering"),
    ("Structured LLM Outputs", "AI / LLM Engineering"),
    ("Function/Tool Calling", "AI / LLM Engineering"),
    ("AI Agent Architecture", "AI / LLM Engineering"),

    # Security
    ("JWT", "Security"),
    ("OAuth2 Bearer Authentication", "Security"),
    ("bcrypt", "Security"),

    # DevOps & Cloud
    ("AWS", "DevOps & Cloud"),
    ("Docker", "DevOps & Cloud"),
    ("GitHub Actions (CI/CD)", "DevOps & Cloud"),
    ("Linux", "DevOps & Cloud"),

    # Testing & Tools
    ("pytest", "Testing & Tools"),
    ("Postman", "Testing & Tools"),
    ("Git", "Testing & Tools"),
    ("GitHub", "Testing & Tools"),
    ("Virtual Environments", "Testing & Tools"),
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
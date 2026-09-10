from datetime import date

from sqlalchemy import delete
from sqlalchemy.orm import Session

from backend.app.db.database import engine
from backend.app.models.experience import Experience


experiences = [
    {
        "company": "Intelligenie LLC",
        "role": "Software Engineer",
        "location": "United States",
        "start_date": date(2026, 2, 1),
        "end_date": None,
        "description": (
            "Primarily working on Python backend development, REST APIs, "
            "and database-related functionality. Developing and modifying "
            "backend services, troubleshooting application issues, making "
            "targeted changes across multiple software projects, and "
            "working with existing codebases and development workflows."
        ),
    },
    {
        "company": "EPAM Systems India Private Limited",
        "role": "Junior Software Engineer",
        "location": "India",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 6, 1),
        "description": (
            "Worked as part of a 20-person software development team "
            "supporting customer and order management functionality for "
            "a high-volume catering platform. Developed and maintained "
            "application functionality using ASP.NET MVC and Object-Oriented "
            "Programming, while participating in Agile development, testing, "
            "debugging, Git-based workflows, and code reviews."
        ),
    },
]


with Session(bind=engine) as db:
    db.execute(delete(Experience))
    for experience_data in experiences:
        experience = Experience(**experience_data)
        db.add(experience)

    db.commit()

    print(f"Inserted {len(experiences)} experiences.")
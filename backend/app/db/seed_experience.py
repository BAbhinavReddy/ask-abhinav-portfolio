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
            "Developing and maintaining Python backend applications, "
            "REST APIs, and database-driven services. Debugging issues, "
            "implementing changes, and working across multiple software projects."
        ),
    },
    {
        "company": "EPAM Systems",
        "role": "Junior Software Engineer",
        "location": "India",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 6, 1),
        "description": (
            "Worked on backend development using C#, .NET, REST APIs, "
            "Entity Framework, PostgreSQL, Git, and Agile development practices."
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
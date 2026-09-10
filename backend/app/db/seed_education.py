from sqlalchemy.orm import Session

from sqlalchemy import delete

from backend.app.db.database import engine
from backend.app.models.education import Education


education = [
    {
        "institution": "University of Missouri-Kansas City",
        "degree": "Master of Science",
        "field_of_study": "Computer Science",
        "gpa": 3.8,
        "start_year": 2024,
        "end_year": 2025,
    },
    {
        "institution": "Vidya Jyothi Institute of Technology",
        "degree": "Bachelor of Technology",
        "field_of_study": "Computer Science Engineering",
        "gpa": 3.48,
        "start_year": 2019,
        "end_year": 2023,
    },
]


with Session(bind=engine) as db:
    db.execute(delete(Education))
    for education_data in education:
        record = Education(**education_data)
        db.add(record)

    db.commit()

    print(f"Inserted {len(education)} education records.")
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.db.session import get_db
from backend.app.models.experience import Experience
from backend.app.schemas.experience import ExperienceResponse


router = APIRouter()


@router.get(
    "/experience",
    response_model=list[ExperienceResponse],
)
def get_experience(db: Session = Depends(get_db)):
    statement = select(Experience).order_by(
        Experience.start_date.desc()
    )

    result = db.execute(statement)

    experiences = result.scalars().all()

    return experiences
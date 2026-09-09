from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.db.session import get_db
from backend.app.models.education import Education
from backend.app.schemas.education import EducationResponse


router = APIRouter()


@router.get(
    "/education",
    response_model=list[EducationResponse],
)
def get_education(db: Session = Depends(get_db)):
    statement = select(Education).order_by(Education.start_year.desc())

    result = db.execute(statement)

    education = result.scalars().all()

    return education
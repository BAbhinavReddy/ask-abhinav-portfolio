from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.db.session import get_db
from backend.app.models.skill import Skill
from backend.app.schemas.skill import SkillResponse


router = APIRouter()


@router.get(
    "/skills",
    response_model=list[SkillResponse],
)
def get_skills(db: Session = Depends(get_db)):
    statement = select(Skill).order_by(Skill.id)

    result = db.execute(statement)

    skills = result.scalars().all()

    return skills
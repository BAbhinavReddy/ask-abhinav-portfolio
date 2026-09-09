from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.db.session import get_db
from backend.app.models.project import Project
from backend.app.schemas.project import ProjectResponse


router = APIRouter()


@router.get(
    "/projects",
    response_model=list[ProjectResponse],
)
def get_projects(db: Session = Depends(get_db)):
    statement = select(Project).order_by(Project.id)

    result = db.execute(statement)

    projects = result.scalars().all()

    return projects
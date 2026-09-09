from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.db.session import get_db
from backend.app.models.profile import Profile
from backend.app.schemas.profile import ProfileResponse


router = APIRouter()


@router.get(
    "/profile",
    response_model=ProfileResponse,
)
def get_profile(db: Session = Depends(get_db)):
    statement = select(Profile)

    result = db.execute(statement)

    profile = result.scalars().first()

    if profile is None:
        raise HTTPException(
            status_code=404, 
            detail="Profile not found",
            )

    return profile
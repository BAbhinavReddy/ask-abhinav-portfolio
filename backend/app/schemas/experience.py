from datetime import date

from pydantic import BaseModel, ConfigDict


class ExperienceResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company: str
    role: str
    location: str
    start_date: date
    end_date: date | None
    description: str
from pydantic import BaseModel, ConfigDict


class EducationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    institution: str
    degree: str
    field_of_study: str
    gpa: float | None
    start_year: int
    end_year: int | None
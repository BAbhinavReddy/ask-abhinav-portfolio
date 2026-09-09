from sqlalchemy import text

from backend.app.db.database import Base, engine
from backend.app.models.profile import Profile
from backend.app.models.skill import Skill
from backend.app.models.experience import Experience
from backend.app.models.project import Project
from backend.app.models.education import Education


Base.metadata.create_all(bind=engine)


with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    print(result.scalar())
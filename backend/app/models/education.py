from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.db.database import Base


class Education(Base):
    __tablename__ = "education"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    institution: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    degree: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    field_of_study: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    start_year: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    end_year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )
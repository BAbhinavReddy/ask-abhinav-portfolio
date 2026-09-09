from datetime import date

from sqlalchemy import Date, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.db.database import Base


class Experience(Base):
    __tablename__ = "experience"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    company: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    role: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    location: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    end_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
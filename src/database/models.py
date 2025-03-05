from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
    )


class User(Base):
    __tablename__ = "user"

    pk: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[str] = mapped_column(String(100), unique=True)
    username: Mapped[str] = mapped_column(String(100), nullable=True)

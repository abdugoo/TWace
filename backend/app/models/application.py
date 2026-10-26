from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Enum, DateTime
from typing import TYPE_CHECKING
from app.enums.app_status import Status
from datetime import datetime, timezone

if TYPE_CHECKING:
    from app.models.user import User


class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )
    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )
    company_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    position: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    status: Mapped[Status] = mapped_column(
        Enum(Status),
        default=Status.SAVED,
        nullable=False
    )
    applied_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default= lambda: datetime.now(timezone.utc),
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default= lambda: datetime.now(timezone.utc),
        onupdate= lambda: datetime.now(timezone.utc),
        nullable=False
    )

    #connection with user
    user: Mapped["User"] = relationship(
        back_populates="applications"
    )
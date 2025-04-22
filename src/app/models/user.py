import uuid
from datetime import datetime

from sqlalchemy import DateTime, func
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyPG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import SQLAlchemyBaseModel


class User(SQLAlchemyBaseModel):
    __tablename__ = "users"

    session_id: Mapped[uuid.UUID] = mapped_column(
        SQLAlchemyPG_UUID(),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        server_onupdate=func.now(),
    )

    parcels: Mapped[list["Parcel"]] = relationship(
        back_populates="user", cascade="all, delete", passive_deletes=True
    )

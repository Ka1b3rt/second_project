import enum
import uuid
from datetime import datetime

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    Enum,
    ForeignKey,
    Numeric,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import SQLAlchemyBaseModel
from .user import User


class TypeType(str, enum.Enum):
    WEAR = "wear"
    ELECTRONICS = "electronics"
    OTHER = "other"



class Parcel(SQLAlchemyBaseModel):
    __tablename__ = "parcel"
    __table_args__ = (
        CheckConstraint(
            f"type_id > 0 AND type_id <= {len(TypeType)}", name="check_type_id"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    weight: Mapped[float] = mapped_column(Numeric(precision=5, scale=2), nullable=False)
    type_id: Mapped[int] = mapped_column(ForeignKey("parcel_type.id"), nullable=False)
    cost: Mapped[float] = mapped_column(Numeric(precision=8, scale=2), nullable=False)
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.session_id", ondelete="CASCADE"),
        nullable=False,
    )
    delivery_price: Mapped[float] = mapped_column(
        Numeric(precision=8, scale=2), nullable=True
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

    type: Mapped["ParcelType"] = relationship(back_populates="parcels")

    user: Mapped["User"] = relationship(back_populates="parcels")


class ParcelType(SQLAlchemyBaseModel):
    __tablename__ = "parcel_type"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped["TypeType"] = mapped_column(
        Enum(TypeType), unique=True, nullable=False
    )

    parcels: Mapped[list["Parcel"]] = relationship(
        back_populates="type", cascade="all, delete", passive_deletes=True
    )

from datetime import datetime

from app.models.parcel import TypeType
from pydantic import UUID4, confloat, conint, field_validator

from .base import BaseSchemaModel


class GetParcelTypes(BaseSchemaModel):
    id: int
    type: TypeType


class GetParcel(BaseSchemaModel):
    id: int
    name: str
    weight: float
    type_id: int
    cost: float
    user_id: UUID4
    delivery_price: float | str
    created_at: datetime
    updated_at: datetime

    @field_validator("delivery_price", mode="before")
    @classmethod
    def replace_delivery_price(cls, value):
        return "Не рассчитано" if value is None else value


class GetParcelById(BaseSchemaModel):
    name: str
    weight: float
    type_id: int
    cost: float
    delivery_price: float


class AddParcel(BaseSchemaModel):
    name: str
    weight: confloat(gt=0)
    type_id: conint(ge=1, le=3)
    cost: confloat(gt=0)


class AddParcelResp(BaseSchemaModel):
    id: int

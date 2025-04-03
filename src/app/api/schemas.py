from pydantic import BaseModel, field_validator
from uuid import UUID

class ParcelCreate(BaseModel):
    name: str
    weight: float
    type_id: int
    value_usd: float

    @field_validator("weight", "value_usd")
    def must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Значение должно быть положительным")
        return v

class ParcelOut(BaseModel):
    id: UUID
    name: str
    weight: float
    type_name: str
    value_usd: float
    delivery_cost_rub: float | None
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ParcelType(Base):
    __tablename__ = "parcel_types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

class Parcel(Base):
    __tablename__ = "parcels"
    id = Column(String, primary_key=True, index=True)  # UUID как строка
    session_id = Column(String, index=True)  # Для привязки к сессии
    name = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    type_id = Column(Integer, ForeignKey("parcel_types.id"), nullable=False)
    value_usd = Column(Float, nullable=False)
    delivery_cost_rub = Column(Float, nullable=True)
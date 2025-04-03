from fastapi import APIRouter, Depends, HTTPException
from uuid import uuid4
import aio_pika
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.schemas import ParcelCreate, ParcelOut
from app.db.database import get_db
from app.db.crud import create_parcel, get_parcel_types
from app.core.config import settings

router = APIRouter()

async def get_session_id():  # Заглушка для сессии
    return "test-session"

async def get_rabbit_connection():
    return await aio_pika.connect_robust(settings.RABBITMQ_URL)

@router.post("/parcels/register")
async def register_parcel(
    parcel: ParcelCreate, session_id: str = Depends(get_session_id)
):
    parcel_id = str(uuid4())
    parcel_data = parcel.dict()
    parcel_data["id"] = parcel_id
    connection = await get_rabbit_connection()
    async with connection:
        channel = await connection.channel()
        await channel.default_exchange.publish(
            aio_pika.Message(body=str(parcel_data).encode()),
            routing_key="parcel_registration",
        )
    return {"parcel_id": parcel_id, "message": "Посылка зарегистрирована"}

@router.get("/parcel-types")
async def list_parcel_types(db: AsyncSession = Depends(get_db)):
    types = await get_parcel_types(db)
    return [{"id": t.id, "name": t.name} for t in types]
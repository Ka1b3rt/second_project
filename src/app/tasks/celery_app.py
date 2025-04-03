from celery import Celery
from app.core.config import settings
from app.db.database import get_db
from app.services.delivery import calculate_delivery_cost
from sqlalchemy.future import select
from app.db.models import Parcel

celery = Celery("tasks", broker=settings.REDIS_URL, backend=settings.REDIS_URL)

@celery.task
async def calculate_delivery_costs():
    async with get_db() as db:
        result = await db.execute(select(Parcel).where(Parcel.delivery_cost_rub.is_(None)))
        parcels = result.scalars().all()
        for parcel in parcels:
            parcel.delivery_cost_rub = await calculate_delivery_cost(parcel.weight, parcel.value_usd)
        await db.commit()
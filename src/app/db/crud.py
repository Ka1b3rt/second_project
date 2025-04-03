from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Parcel, ParcelType

async def create_parcel(db: AsyncSession, parcel_data: dict, session_id: str):
    parcel = Parcel(**parcel_data, session_id=session_id)
    db.add(parcel)
    await db.commit()
    await db.refresh(parcel)
    return parcel

async def get_parcel_types(db: AsyncSession):
    result = await db.execute(select(ParcelType))
    return result.scalars().all()
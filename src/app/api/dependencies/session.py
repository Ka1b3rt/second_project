from typing import AsyncGenerator

from app.core.database import async_db
from sqlalchemy.ext.asyncio import AsyncSession


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_db.session_factory() as session:
        yield session

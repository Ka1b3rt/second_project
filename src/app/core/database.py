from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker


class AsyncDatabase:
    def __init__(self):
        self.postgres_uri: str = settings.postgres.DATABASE_ASYNC_URL
        self.engine: AsyncEngine = create_async_engine(
            url=self.postgres_uri,
            echo=settings.postgres.PG_ECHO,
            pool_size=settings.postgres.PG_POOL_SIZE,
            max_overflow=settings.postgres.PG_MAX_OVERFLOW,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine, expire_on_commit=False
        )


class SyncDatabase:
    def __init__(self):
        self.postgres_uri: str = settings.postgres.DATABASE_SYNC_URL
        self.engine = create_engine(
            url=self.postgres_uri,
            echo=settings.postgres.PG_ECHO,
            pool_size=settings.postgres.PG_POOL_SIZE,
            max_overflow=settings.postgres.PG_MAX_OVERFLOW,
        )
        self.session_factory = sessionmaker(bind=self.engine, expire_on_commit=False)


async_db: AsyncDatabase = AsyncDatabase()
sync_db: SyncDatabase = SyncDatabase()

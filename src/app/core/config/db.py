from app.core.config.base import BaseConfig
from app.core.mixin import BaseUrlBuilderMixin


class PostgresConfig(BaseConfig, BaseUrlBuilderMixin):
    """Конфигурация для PostgreSQL."""
    
    PG_HOST: str
    PG_PORT: int
    PG_USER: str
    PG_PASSWORD: str
    PG_DB: str
    PG_ECHO: bool = False
    PG_POOL_SIZE: int = 5
    PG_MAX_OVERFLOW: int = 10
    
    @property
    def DATABASE_ASYNC_URL(self) -> str:
        """Возвращает URL для асинхронного подключения к БД."""
        return self.build_url(
            scheme="postgresql+asyncpg",
            user=self.PG_USER,
            password=self.PG_PASSWORD,
            host=self.PG_HOST,
            port=self.PG_PORT,
            path=self.PG_DB,
        )
    
    @property
    def DATABASE_SYNC_URL(self) -> str:
        """Возвращает URL для синхронного подключения к БД."""
        return self.build_url(
            scheme="postgresql+psycopg2",
            user=self.PG_USER,
            password=self.PG_PASSWORD,
            host=self.PG_HOST,
            port=self.PG_PORT,
            path=self.PG_DB,
        ) 
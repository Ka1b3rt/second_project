from app.core.config.base import BaseConfig
from app.core.mixin import BaseUrlBuilderMixin


class RedisConfig(BaseConfig, BaseUrlBuilderMixin):
    """Конфигурация для Redis."""
    
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_USER: str
    REDIS_PASSWORD: str
    
    REDIS_QUEUE: int = 0
    REDIS_RESULTS: int = 1
    REDIS_CACHE: int = 2
    
    def _get_redis_url(self, db: int) -> str:
        """Строит URL для подключения к Redis."""
        return self.build_url(
            scheme="redis",
            user=self.REDIS_USER,
            password=self.REDIS_PASSWORD,
            host=self.REDIS_HOST,
            port=self.REDIS_PORT,
            path=str(db),
        )
    
    @property
    def REDIS_URL_QUEUE(self) -> str:
        """Возвращает URL для очереди Redis."""
        return self._get_redis_url(self.REDIS_QUEUE)
    
    @property
    def REDIS_URL_RESULTS(self) -> str:
        """Возвращает URL для результатов Redis."""
        return self._get_redis_url(self.REDIS_RESULTS)
    
    @property
    def REDIS_URL_CACHE(self) -> str:
        """Возвращает URL для кэша Redis."""
        return self._get_redis_url(self.REDIS_CACHE) 
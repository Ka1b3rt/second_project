from app.core.config.api import ApiConfig
from app.core.config.db import PostgresConfig
from app.core.config.redis import RedisConfig
from app.core.config.rabbitmq import RabbitMQConfig


class Settings:
    """Основной класс настроек приложения."""
    
    def __init__(self):
        self.api = ApiConfig()
        self.postgres = PostgresConfig()
        self.redis = RedisConfig()
        self.rabbitmq = RabbitMQConfig()


# Создаем глобальный экземпляр настроек
settings = Settings() 
from app.core.config.base import BaseConfig


class RabbitMQConfig(BaseConfig):
    """Конфигурация для RabbitMQ."""
    
    RABBITMQ_HOST: str
    RABBITMQ_PORT: int
    RABBITMQ_MANAGEMENT_PORT: int
    RABBITMQ_USER: str
    RABBITMQ_PASSWORD: str
    RABBITMQ_VHOST: str
    
    @property
    def RABBITMQ_URL(self) -> str:
        """Возвращает URL для подключения к RabbitMQ."""
        return f"amqp://{self.RABBITMQ_USER}:{self.RABBITMQ_PASSWORD}@{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}/{self.RABBITMQ_VHOST}"
    
    @property
    def RABBITMQ_MANAGEMENT_URL(self) -> str:
        """Возвращает URL для управления RabbitMQ."""
        return f"http://{self.RABBITMQ_HOST}:{self.RABBITMQ_MANAGEMENT_PORT}" 
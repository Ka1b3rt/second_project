from aio_pika import connect_robust
from aio_pika.abc import AbstractRobustConnection
from app.core.config import settings


async def get_rabbitmq_connection() -> AbstractRobustConnection:
    connection = await connect_robust(
        host=settings.rabbitmq.RABBITMQ_HOST,
        port=settings.rabbitmq.RABBITMQ_PORT,
        login=settings.rabbitmq.RABBITMQ_USER,
        password=settings.rabbitmq.RABBITMQ_PASSWORD,
        virtualhost=settings.rabbitmq.RABBITMQ_VHOST,
    )
    return connection

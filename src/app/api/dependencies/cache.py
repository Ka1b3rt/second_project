from app.core.config import settings

from redis.asyncio import Redis


def get_redis_client() -> Redis:
    client = Redis(
        host=settings.redis.REDIS_HOST,
        port=settings.redis.REDIS_PORT,
        username=settings.redis.REDIS_USER,
        password=settings.redis.REDIS_PASSWORD,
        db=settings.redis.REDIS_CACHE,
        decode_responses=True,
    )
    return client

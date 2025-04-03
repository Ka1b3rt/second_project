import aiohttp
import redis.asyncio as redis
from app.core.config import settings

async def get_usd_rub_rate():
    r = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)
    rate = await r.get("usd_rub_rate")
    if not rate:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.cbr-xml-daily.ru/daily_json.js") as resp:
                data = await resp.json()
                rate = data["Valute"]["USD"]["Value"]
                await r.setex("usd_rub_rate", 3600, rate)
    return float(rate)
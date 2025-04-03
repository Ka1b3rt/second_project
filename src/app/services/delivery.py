from app.services.currency import get_usd_rub_rate

async def calculate_delivery_cost(weight: float, value_usd: float) -> float:
    rate = await get_usd_rub_rate()
    return (weight * 0.5 + value_usd * 0.01) * rate
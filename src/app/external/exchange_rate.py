import httpx
from pydantic import ValidationError

from pydantic import BaseModel
from typing import Dict
from datetime import datetime


class CurrencyInfo(BaseModel):
    CharCode: str
    Value: float


class CBRResponse(BaseModel):
    Date: datetime
    Valute: Dict[str, CurrencyInfo]
    
URL = "https://www.cbr-xml-daily.ru/daily_json.js"
    
async def get_usd_to_rub_rate() -> float:
    async with httpx.AsyncClient() as client:
        response = await client.get(URL, timeout=5)
        response.raise_for_status()

    try:
        cbr_data = CBRResponse.model_validate(response.json())
    except ValidationError as e:
        raise RuntimeError("CBR response validation failed") from e

    usd = cbr_data.Valute.get("USD")
    if not usd:
        raise ValueError("USD not found in CBR response")

    return usd.Value

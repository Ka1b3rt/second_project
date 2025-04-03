import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.mark.asyncio
async def test_register_parcel():
    client = TestClient(app)
    response = await client.post("/parcels/register", json={
        "name": "Test",
        "weight": 1.0,
        "type_id": 1,
        "value_usd": 10.0
    })
    assert response.status_code == 200
    assert "parcel_id" in response.json()
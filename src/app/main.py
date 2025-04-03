from fastapi import FastAPI
from app.api.endpoints import router
from app.db.database import init_db
import asyncio

app = FastAPI(title="Delivery Service")

@app.on_event("startup")
async def startup_event():
    await init_db()

app.include_router(router)
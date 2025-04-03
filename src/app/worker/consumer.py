import asyncio
import aio_pika
from app.core.config import settings
from app.db.database import get_db
from app.db.crud import create_parcel
import json

async def process_message(message: aio_pika.IncomingMessage):
    async with message.process():
        parcel_data = json.loads(message.body.decode())
        session_id = parcel_data.pop("session_id", "unknown")
        async with get_db() as db:
            await create_parcel(db, parcel_data, session_id)

async def main():
    connection = await aio_pika.connect_robust(settings.RABBITMQ_URL)
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("parcel_registration")
        await queue.consume(process_message)
        await asyncio.Future() 
        
if __name__ == "__main__":
    asyncio.run(main())
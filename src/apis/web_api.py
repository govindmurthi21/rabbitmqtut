from fastapi import APIRouter, HTTPException
from src.producers.producer import produce
from src.consumers.consumer import run as run_consumers

from src.models.message import Message

router = APIRouter()

@router.post('/message')
async def produce_message(message: Message):
    produce(message=message.message)
    return f'Message produced'

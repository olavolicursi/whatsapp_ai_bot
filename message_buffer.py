import redis.asyncio as redis
import asyncio

from collections import defaultdict

from config import REDIS_URL, BUFFER_KEY_SUFIX, DEBOUNCE_SECONDS, BUFFER_TTL
from evolution_api import send_whatsapp_message
from chains import get_conversational_rag_chain

redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)
conversational_rag_chain = get_conversational_rag_chain()
debounce_tasks = defaultdict(asyncio.Task)

def log(*args):
    print('[BUFFER]', *args)

async def buffer_message(chat_id: str, message: str):
    buffer_key = f'{chat_id}{BUFFER_KEY_SUFIX}'

    await redis_client.rpush(buffer_key, message)
    await redis_client.expire(buffer_key, BUFFER_TTL)

    log(f'Mensagem adicionada ao buffer {chat_id}: {message}')

    if debounce_tasks.get(chat_id):
        debounce_tasks[chat_id].cancel()
        log(f'Tarefa de debounce cancelada para {chat_id}')

    debounce_tasks[chat_id] = asyncio.create_task(...)
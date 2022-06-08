import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config



loop = asyncio.get_event_loop()
bot = Bot(token='5549681338:AAF4EwhP-8oA4JSpcOmc2SBuxe9dWe5j4UA', parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


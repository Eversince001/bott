from aiogram import types
import logging
from aiogram.dispatcher.filters.builtin import Command, CommandStart
from aiogram.types import message, reply_keyboard, user
from aiogram.types import CallbackQuery
from loader import dp, bot
#from data.config import ADMINS

from asyncpg import Connection, Record
from asyncpg.exceptions import UniqueViolationError
#from utils.db_api.DBCommands import DBCommands
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types

from keyboards.default.topic import topicMenu
from keyboards.default.subtopic import subtopicDoc,subtopicCalendar
#from states.stateBot import FSMAdder





@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    user_name  =  message.from_user.full_name
    await message.answer(text="Вот, что ты можешь сделать",
                            reply_markup=topicMenu)


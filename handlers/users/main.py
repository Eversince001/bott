from aiogram import types
import logging
from aiogram.dispatcher.filters.builtin import Command, CommandStart
from aiogram.types import message, reply_keyboard, user
from aiogram.types import CallbackQuery
import data
from loader import dp, bot
import final.answer
import final.data
#from data.config import ADMINS

from asyncpg import Connection, Record
from asyncpg.exceptions import UniqueViolationError
#from utils.db_api.DBCommands import DBCommands
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types

from keyboards.default.topic import topicMenu
from keyboards.default.subtopic import subtopicDoc,subtopicCalendar, subtopicCategory, subtopicExams
from keyboards.default.questionDoc import subtopic1Que,subtopic2Que,subtopic3Que,subtopic4Que
from keyboards.default.questionCal import quesction1Cal,  quesction2Cal, quesction3Cal, quesction4Cal
from keyboards.default.questionsCat import quesction1Cat, quesction2Cat, quesction3Cat, quesction4Cat
from keyboards.default.questionExams import question1Exam, question2Exam, question3Exam
from keyboards.default.questionDir import question1Dir
from keyboards.default.questionChange import question1C
from keyboards.default.questionHome import question1Home


from utils.questionsList import questions
from utils.requests import req

Data = final.data.DATA()

@dp.message_handler()
async def bot_message(message: types.Message):

    #Subtopics
    if message.text == "Подача документов":
        await message.answer(text= message.text, reply_markup=subtopicDoc)
        Data.set_part(1)
    if message.text == "Календарь приема":
        await message.answer(text=message.text, reply_markup=subtopicCalendar)
        Data.set_part(2)
    if message.text == "Особые категории":
        await  message.answer(text=message.text, reply_markup=subtopicCategory)
        Data.set_part(3)
    if message.text == "Направление":
        await message.answer(text=message.text, reply_markup=subtopicExams)
        Data.set_part(4)
    if message.text == "Экзамены":
        await message.answer(text=message.text, reply_markup=subtopicExams)
        Data.set_part(5)
    if message.text == "Оценить шансы":
        await message.answer(text=message.text, reply_markup=question1C)
        Data.set_part(6)
    if message.text == "Общежитие":
        await message.answer(text=message.text, reply_markup=question1Home)
        Data.set_part(7)


    #SUBTOPIC 1
    if message.text == "Как подать документы":
        await message.answer(text=message.text, reply_markup=subtopic1Que)
    if message.text == "Необходимый перечень документов":
        await message.answer(text=message.text, reply_markup=subtopic2Que)
    if message.text == "Заключить договор на обучение по контракту":
        await message.answer(text=message.text, reply_markup=subtopic3Que)

    if message.text == "Как подать согласие":
        await message.answer(text=message.text, reply_markup=subtopic4Que)

    #SUBTOPIC 2
    if message.text == "Основные даты":
        await message.answer(text=message.text, reply_markup=quesction1Cal)
    if message.text == "Расписание вступительных испытаний":
        await message.answer(text=message.text, reply_markup=quesction2Cal)
    if message.text == "Приказы о зачислении":
        await message.answer(text=message.text, reply_markup=quesction3Cal)
    if message.text == "Заселение в общежитие":
        await message.answer(text=message.text, reply_markup=quesction4Cal)
    #Subtopic 3
    if message.text == "Льготы":
         await message.answer(text=message.text, reply_markup=quesction1Cat)
    if message.text == "Поступление БВИ":
        await message.answer(text=message.text, reply_markup=quesction2Cat)
    if message.text == "Целевое обучение":
        await message.answer(text=message.text, reply_markup=quesction3Cat)
    if message.text == "Индивидуальные достижения":
        await message.answer(text=message.text, reply_markup=quesction4Cat)
    #Subtopic 4
    if message.text == "Направления":
        await message.answer(text=message.text, reply_markup=question1Dir)

    #Subtopic 5
    if message.text == "По EГЭ":
        await message.answer(text=message.text, reply_markup=question1Exam)
    if message.text == 'Вступительные испытания':
        await message.answer(text=message.text, reply_markup=question2Exam)
    if message.text == "Минимальные баллы":
        await message.answer(text=message.text, reply_markup=question3Exam)


    #Questions
    if message.text in questions:
        logging.info(message.text)
        que = message.text + '?'
        answer = req(que)
        logging.info(answer[0]['answer'])
        await message.answer(text=answer[0]['answer'])
        #await message.answer(text="Я получил вопрос: " + que)
    else:
        answ = final.answer.get_answer(message.text, Data.get_part()) 
        # Отсылаем юзеру сообщение в его чат
        await message.answer(text=answ[0]['answer'])
        Data.set_part(-1)


from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

question1C = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("Как оценить свои шансы поступит на бюджет")
question1C.add(b1)

b1 = KeyboardButton("Какие минимальные баллы для обучения по контракту")
question1C.add(b1)

b1 = KeyboardButton("Где просмотреть рейтинговые списки")
question1C.add(b1)

b1 = KeyboardButton("Какие проходные баллы прошлых лет")
question1C.add(b1)

b1 = KeyboardButton("Сколько бюджетные мест на направлениях")
question1C.add(b1)

b1 = KeyboardButton("Где просмотреть приказы на зачисление")
question1C.add(b1)

b1 = KeyboardButton("Когда издаются приказы на зачисления")
question1C.add(b1)

b1 = KeyboardButton("Можно ли пойти на контракт, если не поступил на бюджет")
question1C.add(b1)

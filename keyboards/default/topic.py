from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

topicMenu = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("Подача документов")
topicMenu.add(b1)

b1 = KeyboardButton("Календарь приема")
topicMenu.add(b1)

b1 = KeyboardButton("Особые категории")
topicMenu.add(b1)

b1 = KeyboardButton("Направления")
topicMenu.add(b1)

b1 = KeyboardButton("Экзамены")
topicMenu.add(b1)

b1 = KeyboardButton("Оценить шансы")
topicMenu.add(b1)

b1 = KeyboardButton("Общежитие")
topicMenu.add(b1)

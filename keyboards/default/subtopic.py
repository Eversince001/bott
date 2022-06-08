from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


subtopicDoc = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("Как подать документы")
subtopicDoc.add(b1)

b1 = KeyboardButton("Необходимый перечень документов")
subtopicDoc.add(b1)

b1 = KeyboardButton("Заключить договор на обучение по контракту")
subtopicDoc.add(b1)

b1 = KeyboardButton("Как подать согласие")
subtopicDoc.add(b1)

subtopicCalendar = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("Основные даты")
subtopicCalendar.add(b1)

b1 = KeyboardButton("Расписание вступительных испытаний")
subtopicCalendar.add(b1)

b1 = KeyboardButton("Приказы о зачислении")
subtopicCalendar.add(b1)

b1 = KeyboardButton("Заселение в общежитие")
subtopicCalendar.add(b1)


subtopicCategory = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("Льготы")
subtopicCategory.add(b1)

b1 = KeyboardButton("Поступление БВИ")
subtopicCategory.add(b1)

b1 = KeyboardButton("Целевое обучение")
subtopicCategory.add(b1)

b1 = KeyboardButton("Индивидуальные достижения")
subtopicCategory.add(b1)

subtopicExams = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("По ЕГЭ")
subtopicExams.add(b1)

b1 = KeyboardButton("Вступительные испытания")
subtopicExams.add(b1)

b1 = KeyboardButton("Минимальные баллы")
subtopicExams.add(b1)



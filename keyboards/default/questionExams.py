from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


question1Exam = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("Какие минимальные баллы ЕГЭ")
question1Exam.add(b1)

b1 = KeyboardButton("Какие ЕГЭ нужно сдавать для разных направлений")
question1Exam.add(b1)

b1 = KeyboardButton("ЕГЭ за какие года действуют")
question1Exam.add(b1)

b1 = KeyboardButton("Где можно сдать ЕГЭ")
question1Exam.add(b1)

b1 = KeyboardButton("Кто имеет права сдавать ЕГЭ")
question1Exam.add(b1)

b1 = KeyboardButton("Нужно ли предоставлять свидетельство с результатами ЕГЭ")
question1Exam.add(b1)

b1 = KeyboardButton("Если я сдал(а) ЕГЭ, нужно ли мне сдавать ВИ")
question1Exam.add(b1)

question2Exam = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("Кто имеет право сдавит ВИ")
question2Exam.add(b1)

b1 = KeyboardButton("Как записаться на сдачу ВИ")
question2Exam.add(b1)

b1 = KeyboardButton("До какого числа необходимо подать документы при поступлении по ВИ")
question2Exam.add(b1)

b1 = KeyboardButton("Где будет происходить сдача ВИ")
question2Exam.add(b1)

b1 = KeyboardButton("В каком формате проходят ВИ")
question2Exam.add(b1)

b1 = KeyboardButton("В какие даты проходят ВИ")
question2Exam.add(b1)

b1 = KeyboardButton("Как проходит апелляция при ВИ")
question2Exam.add(b1)

b1 = KeyboardButton("Что такое система «прокторинга»")
question2Exam.add(b1)

b1 = KeyboardButton("Могу ли я сдать ВИ из дома")
question2Exam.add(b1)

b1 = KeyboardButton("Когда станут известны результаты ВИ")
question2Exam.add(b1)

b1 = KeyboardButton("Где можно найти демоверсии ВИ")
question2Exam.add(b1)

b1 = KeyboardButton("Существует ли инклюзивное сопровождении при сдачи ВИ по материалам ВУЗа")
question2Exam.add(b1)

b1 = KeyboardButton("Могу ли я получить комнату в общежитии на время сдачи ВИ")
question2Exam.add(b1)

question3Exam = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("Какие минимальные баллы необходимо набрать для участия в конкурсе на поступление")
question3Exam.add(b1)

b1 = KeyboardButton("Какие минимальные баллы для обучения по контракту")
question3Exam.add(b1)

b1 = KeyboardButton("*Подобрать направление, с учетом сданных экзаменов")
question3Exam.add(b1)

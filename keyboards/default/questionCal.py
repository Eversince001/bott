from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

quesction1Cal = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("Когда начинается прием документов")
quesction1Cal.add(b1)

b1 = KeyboardButton("Когда заканчивается прием документов")
quesction1Cal.add(b1)

b1 = KeyboardButton("До какого числа можно вносить изменения в заявление")
quesction1Cal.add(b1)

b1 = KeyboardButton("До какого числа необходимо подать согласие")
quesction1Cal.add(b1)

b1 = KeyboardButton("До какого числа можно заключить договор на контрактное обучение")
quesction1Cal.add(b1)

b1 = KeyboardButton("До какого числа необходимо предоставить оригиналы")
quesction1Cal.add(b1)

b1 = KeyboardButton("Когда публикуются приказы о зачислении")
quesction1Cal.add(b1)

quesction2Cal = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("Когда проводятся вступительные испытания по материалам ВУЗа")
quesction2Cal.add(b1)

b1 = KeyboardButton("Когда станут известны результаты экзаменов")
quesction2Cal.add(b1)

b1 = KeyboardButton("Как найти расписание вступительных испытаний")
quesction2Cal.add(b1)

b1 = KeyboardButton("Когда проводится апелляция")
quesction2Cal.add(b1)


quesction3Cal =ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("Когда публикуются приказы о зачислении на бюджетные места")
quesction3Cal.add(b1)

b1 = KeyboardButton("Когда публикуются приказы о зачислении на контрактные места")
quesction3Cal.add(b1)

b1 = KeyboardButton("Когда публикуются приказы о зачислении на места в пределах особой квоты")
quesction3Cal.add(b1)

quesction4Cal = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("Когда нужно подать документы на заселение")
quesction4Cal.add(b1)

b1 = KeyboardButton("Когда будет заселение в общежитие")
quesction4Cal.add(b1)

b1 = KeyboardButton("Могу ли я заселиться раньше/позже")
quesction4Cal.add(b1)

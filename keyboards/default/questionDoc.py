from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

subtopic1Que = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("До какого числа нужно подать документы")
subtopic1Que.add(b1)

b1 = KeyboardButton("Как подать документы через сайт")
subtopic1Que.add(b1)

b1 = KeyboardButton("Как подать документы лично")
subtopic1Que.add(b1)

b1 = KeyboardButton("Как подать документы по почте")
subtopic1Que.add(b1)

b1 = KeyboardButton("Как подать документы через Госуслуги")
subtopic1Que.add(b1)

b1 = KeyboardButton("Как изменить поданное заявление")
subtopic1Que.add(b1)

subtopic2Que = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("Какие документы нужны для поступления по общему конкурсу")
subtopic2Que.add(b1)

b1 = KeyboardButton("Какие документы нужны для целевого приема")
subtopic2Que.add(b1)

b1 = KeyboardButton("Какие документы нужны для приема без экзаменов")
subtopic2Que.add(b1)

b1 = KeyboardButton("Какие документы нужны для приема вне конкурса (особая квота)")
subtopic2Que.add(b1)

b1 = KeyboardButton("Какие документы нужны иностранным гражданам")
subtopic2Que.add(b1)

b1 = KeyboardButton("Нужны ли оригиналы")
subtopic2Que.add(b1)

subtopic3Que = ReplyKeyboardMarkup(resize_keyboard=True)
b1 =KeyboardButton("Что такое обучение по контракту")
subtopic3Que.add(b1)

b1 =KeyboardButton("Где можно взять шаблон договора")
subtopic3Que.add(b1)

b1 =KeyboardButton("До какого числа нужно заключить договор")
subtopic3Que.add(b1)

b1 =KeyboardButton("Кто и как заключает договор")
subtopic3Que.add(b1)

b1 =KeyboardButton("Как можно оплатить (мат. Капитал, оплата онлайн, образовательный кредит)")
subtopic3Que.add(b1)


subtopic4Que = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("Где можно взять шаблон согласия")
subtopic4Que.add(b1)

b1 = KeyboardButton("До какого числа нужно подать согласие")
subtopic4Que.add(b1)

b1 = KeyboardButton("Сколько согласий одновременно можно подать")
subtopic4Que.add(b1)

b1 = KeyboardButton("Можно ли менять поданное согласие")
subtopic4Que.add(b1)

b1 = KeyboardButton("Как подать согласие")
subtopic4Que.add(b1)

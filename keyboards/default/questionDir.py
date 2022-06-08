from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

question1Dir = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("Какие направления есть в НГТУ")
question1Dir.add(b1)

b1 = KeyboardButton("На сколько направлений можно подать документы")
question1Dir.add(b1)

b1 = KeyboardButton("Как поменять направление")
question1Dir.add(b1)

b1 = KeyboardButton("Смогу ли я поменять направление после поступления")
question1Dir.add(b1)

b1 = KeyboardButton("Смогу ли перейти на бюджет, если поступлю на контракт")
question1Dir.add(b1)

b1 = KeyboardButton("До какого числа можно изменить направления в заявлении")
question1Dir.add(b1)

b1 = KeyboardButton("Сколько бюджетных и контарктых мест на напрвлениях")
question1Dir.add(b1)

b1 = KeyboardButton("Какая стоимость обучения по контаркту на разных направлениях")
question1Dir.add(b1)

b1 = KeyboardButton("Какие экзамены нужно сдавать для поступления на различные направления НГТУ")
question1Dir.add(b1)

b1 = KeyboardButton("Подобрать направление, с учетом сданных экзаменов")
question1Dir.add(b1)


from multiprocessing.connection import answer_challenge
import telebot
from telebot import types
import answer
import data
bot = telebot.TeleBot('5549681338:AAF4EwhP-8oA4JSpcOmc2SBuxe9dWe5j4UA')
Data = data.DATA()
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Подача документов")
        item2 = types.KeyboardButton("Календарь приема")
        item3 = types.KeyboardButton("Особые категории")
        item4 = types.KeyboardButton("Направление")
        item5 = types.KeyboardButton("Экзамены")
        item6 = types.KeyboardButton("Оценить шансы")
        item7 = types.KeyboardButton("Общежитие")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        markup.add(item6)
        markup.add(item7)
        bot.send_message(m.chat.id, 'Выбери раздел, из которого хочешь задать вопрос',  reply_markup=markup)

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
        # Если юзер прислал 1, выдаем ему случайный факт
        if ((message.text.strip() == 'Подача документов' or message.text.strip() == '1') and Data.get_part() == 0):
                bot.send_message(message.chat.id, "Задай вопрос")
                Data.set_part(1)
                return
        # Если юзер прислал 2, выдаем умную мысль
        elif ((message.text.strip() == 'Календарь приема' or message.text.strip() == '2') and Data.get_part() == 0):
                bot.send_message(message.chat.id, "Задай вопрос")
                Data.set_part(2)
                return
        elif ((message.text.strip() == 'Особые категории' or message.text.strip() == '3') and Data.get_part() == 0):
                bot.send_message(message.chat.id, "Задай вопрос")
                Data.set_part(3)
                return
        elif ((message.text.strip() == 'Направление' or message.text.strip() == '4') and Data.get_part() == 0):
                bot.send_message(message.chat.id, "Задай вопрос")
                Data.set_part(4)
                return
        elif ((message.text.strip() == 'Экзамены' or message.text.strip() == '5') and Data.get_part() == 0):
                bot.send_message(message.chat.id, "Задай вопрос")
                Data.set_part(5)
                return
        elif ((message.text.strip() == 'Оценить шансы' or message.text.strip() == '6') and Data.get_part() == 0):
                bot.send_message(message.chat.id, "Задай вопрос")
                Data.set_part(6)
                return
        elif ((message.text.strip() == 'Общежитие' or message.text.strip() == '7') and Data.get_part() == 0):
                bot.send_message(message.chat.id, "Задай вопрос")
                Data.set_part(7)
                return

        answ = answer.get_answer(message.text, Data.get_part()) 
        # Отсылаем юзеру сообщение в его чат
        bot.send_message(message.chat.id, answ)
        Data.set_part(0)

# Запускаем бота
bot.polling(none_stop=True, interval=0)
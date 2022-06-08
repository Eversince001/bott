import string
from pyaspeller import YandexSpeller
from pymystem3 import Mystem

#speller - переменная класса YandexSpeller, отвечающая за корректировку ошибок в сообщениях
#m - переменная класса Mystem, отвечающая за лемматизацию сообщения
speller = YandexSpeller()
m = Mystem()

#Удаление символов пунктуации
def remove_punctuation(text):
       translator = str.maketrans('', '', string.punctuation)
       return text.translate(translator)

#Лемматизация
def diction_form(text):
       text = ''.join(m.lemmatize(text)).rstrip('\n')
       return text

#Функция предобработки сообщения пользователя
#Замена буквы "ё" на "е", корректировка ошибок с помощью speller
#Удаление знаков пунктуации и прочих символов, которые не являются буквами
#Приведение каждого слова сообщения к нормальной форме
def correct_message(msg):
    print("Исходная строка: " + msg)
    msg = str(msg).lower().replace("ё", "е")
    print("Замена буквы Ё: " + msg)
    msg = speller.spelled(msg)
    print("Коррекция ошибок: " + msg)
    msg = remove_punctuation(msg.lower())
    print("Удаление знаков пунктуации: " + msg)
    msg = diction_form(msg)
    print("Приведение слова к нормальной форме: " + msg)
    print('\n')
    return msg
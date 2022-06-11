import string
from pyaspeller import YandexSpeller
from pymystem3 import Mystem
import logging
import final.bd
from flashtext import KeywordProcessor

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

#Замена слов на синонимы, которые хранятся в словаре
def syn(question):
       synonyms = final.bd.get_synonyms()
       #keyword_processor - переменная класса KeywordProcessor, отвечающаю за замену слов на синоним из базы данных синонимов
       keyword_processor = KeywordProcessor()
       keyword_processor.add_keywords_from_dict(synonyms)

       msg = ""
       for i in range(len(question)):
              question[i] = keyword_processor.replace_keywords(question[i])
              if (i != len(question) - 1):
                     msg += question[i] + " "
              else:
                     msg += question[i]
       return msg
       

#Функция предобработки сообщения пользователя
#Замена буквы "ё" на "е", корректировка ошибок с помощью speller
#Удаление знаков пунктуации и прочих символов, которые не являются буквами
#Приведение каждого слова сообщения к нормальной форме
def correct_message(msg):
       tmp = msg
       logging.info("Исходная строка: " + tmp)
       msg = str(msg).lower().replace("ё", "е")
       logging.info("Замена буквы Ё: " + msg)
       msg = speller.spelled(msg)
       logging.info("Коррекция ошибок: " + msg)
       msg = remove_punctuation(msg.lower())
       logging.info("Удаление знаков пунктуации: " + msg)
       msg = syn(msg.split())
       logging.info("Замена слов на синонимы: " + msg)
       msg = diction_form(msg)
       logging.info("Приведение слова к нормальной форме: " + msg)

       return msg
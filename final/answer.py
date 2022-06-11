from itertools import groupby
import pymorphy2
import final.bd
from final.correction import correct_message
from utils.requests import req
import logging


def get_answer(msg, part):

       #morph - переменная класса MorphAnalyzer, отвечающая за морфологический анализ слов
       morph = pymorphy2.MorphAnalyzer()

       #necessary_part - список частей речи, которые будут оставлены в сообщении пользователя после обработки 
       necessary_part = {"NOUN", "ADJF", "ADJS", "VERB", "INFN", "PRTF", "PRTS", "GRND", "ADVB", "PRED"}

       #Загрузка баз данных из файлов
       #db - массив, содержащий вопросы
       db = final.bd.get_questions()
       db_clear = final.bd.get_clear_questions()


       #accuracy - точность нахождения ответа на вопрос пользователя
       #tmp - временная переменная, необходимая для сравнения точности последнего найденого ответа с текущей точностью accuracy
       #answer - ответ на вопрос пользователя, по умолчанию стоит заглушка
       accuracy = 1
       tmp = 0
       answer = "Я вас не понял, попробуйте переформулировать вопрос"


       #Обработка сообщения пользователя 
       msg = correct_message(msg)
       #Разбиение сообщения пользователя на слова 
       #и занесение их в массив question с его последующей сортировкой
       question = msg.split()
       question.sort()
       question = [el for el, _ in groupby(question)]

       _question = []

       #Обработка полученного сообщения, удаление из него ненужных частей речи,
       #которых нет в списке necessary_part
       for el in question:
            p = morph.parse(el)[0]
            if p.tag.POS in necessary_part or el == "когда" or el == "как":
                _question.append(p.normal_form)
       question = _question


       #Нахождение ответа на вопрос пользователя путем определения
       #самого схожего вопроса в базе данных с вопросом пользователя
        
       if (part != -1): 
              for k in range(0, len(db[part - 1])):
                     qst = db[part-1][k].split()
                     for j in range(0, len(question)):
                            if(question[j] in qst):
                                   tmp += 1
                     if(tmp > accuracy):
                            accuracy = tmp
                            answer = db_clear[part - 1][k]
                     tmp = 0
       else:
              for i in range(0, len(db)):
                     for k in range(0, len(db[i])):
                            qst = db[i][k].split()
                            for j in range(0, len(question)):
                                   if(question[j] in qst):
                                          tmp += 1
                            if(tmp > accuracy):
                                   accuracy = tmp
                                   answer = db_clear[i][k]
                            tmp = 0
       logging.info(answer)
       answer = req(answer)
       return answer

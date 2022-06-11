#Чтение списка ответов из файла
from asyncio import QueueEmpty


def get_answers():
    dbA = []
    iterator = 1
    for i in range(7):
        dbA.append([])

    f = open("final/baseA.txt", 'r', encoding="utf-8")
    for line in f:
        if(len(line) == 2):
                iterator = int(line[0])
                continue
        dbA[iterator - 1].append(line)
    f.close()
    return dbA

#Чтение списка синонимов из файла
def get_synonyms():
    synonyms = dict()
    f = open("final/dict.txt", 'r', encoding="utf-8")
    for line in f:
        words = line.split()
        tmp = words[0]
        words.remove(words[0])
        synonyms[tmp] = words
    return synonyms

#Чтение списка вопрсов из файла
def get_questions():
    questions = [
        [
            "до какой число нужно подавать документ",
            "как подавать документ через сайт",
            "как подавать документ лично",
            "как подавать документ по почта",
            "как подавать документ через госуслуга",
            "как изменять подавать заявление",
            "какой документ нужный для поступление по общий конкурс",
            "какой документ нужный для целевой прием",
            "какой документ нужный для прием без экзамен",
            "какой документ нужный для прием вне конкурс особый квота",
            "какой документ нужный иностранный гражданин",
            "нужный ли оригинал",
            "что такой обучение по контракт",
            "где можно взять шаблон договор",
            "до какой число нужно заключать договор",
            "кто и как заключать договор ",
            "как можно оплачивать обучение контракт",
            "где можно взять шаблон согласие",
            "до какой число нужно подавать согласие",
            "сколько согласие одновременно можно подавать",
            "можно ли менять подавать согласие",
            "как подавать согласие"
        ],
        [
            "когда начинаться прием документ",
            "когда заканчиваться прием документ",
            "до какой число можно вносить изменение в заявление",
            "до какой число необходимо подавать согласие ",
            "до какой число можно заключать договор на контрактный обучение",
            "до какой число необходимо предоставлять оригинал",
            "когда публиковаться приказ о зачисление",
            "когда проводиться вступительный испытание по материал вуз",
            "когда становиться известный результат экзамен",
            "как находить расписание вступительный испытание",
            "когда проводиться апелляция",
            "когда публиковаться приказ о зачисление на бюджетный место",
            "когда публиковаться приказ о зачисление на контрактный место",
            "когда публиковаться приказ о зачисление на место в предел особый квота",
            "когда нужно подавать документ на заселение",
            "когда быть заселение в общежитие",
            "мочь ли я заселяться раньше поздно"
        ],
        [
            "какой льгота устанавливать правило прием",
            "какой документ подавать при поступление по льгота",
            "до какой число необходимо подавать документ по льгота",
            "можно ли сдавать вступительный испытание по материал вуз если я поступать по льгота",
            "какой минимальный балл егэ нужный при поступление по льгота",
            "когда издаваться приказ о зачисление по льгота",
            "быть ли инклюзивный сопровождение при поступление в нгт",
            "на какой направление действовать льготный право поступление",
            "на сколько направление действовать льготный право поступление",
            "кто мочь поступать без вступительный испытание",
            "до какой число необходимо подавать документ при поступление бви",
            "какой документ подавать при поступление бви",
            "нужно ли иметь результат егэ при поступление бви",
            "можно ли воспользоваться право поступление бви если сдавать вступительный испытание по материал вуз",
            "когда издаваться приказ о зачисление бви",
            "на сколько направление действовать право поступление бви",
            "что такой целевой обучение",
            "кто заключать договор на целевой обучение",
            "где взять шаблон договор на целевой обучение",
            "как заключать договор на целевой обучение",
            "какой документ необходимо подавать при поступление на целевой обучение",
            "до какой число необходимо подавать документ при поступление на целевой обучение",
            "когда издаваться приказ о зачисление на целевой обучение",
            "какой индивидуальный достижение засчитываться при поступление",
            "сколько балл можно получать за индивидуальный достижение",
            "до какой число необходимо предоставлять документ подтверждать наличие индивидуальный достижение",
            "как предоставлять документ подтверждать наличие индивидуальный достижение",
            "за какой год действовать индивидуальный достижение",
        ],
        [
            "какой направление быть в нгт",
            "на сколько направление можно подавать документ",
            "как поменять направление",
            "смочь ли я поменять направление после поступление",
            "смочь ли переходить на бюджет если поступать на контракт",
            "до какой число можно изменять направление в заявление",
            "сколько бюджетный и контарктых место на напрвление",
            "какой стоимость обучение по контракт на разный направление",
            "какой экзамен нужно сдавать для поступление на различный направление нгт",
            "подбирать направление с учет сдавать экзамен",
        ],
        [
            "какой минимальный балл егэ",
            "какой егэ нужно сдавать для разный направление",
            "егэ за какой год действовать",
            "где можно сдавать егэ",
            "кто иметь право сдавать егэ",
            "нужно ли предоставлять свидетельство с результат егэ",
            "если я сдавать егэ нужно ли я сдавать вступительный экзамен",
            "кто иметь право сдавать вступительный экзамен",
            "как записываться на сдача вступительный экзамен",
            "до какой число необходимо подавать документ при поступление по вступительный экзамен",
            "где быть происходить сдача вступительный экзамен",
            "в какой формат проходить вступительный экзамен",
            "в какой дата проходить вступительный экзамен расписание",
            "как проходить апелляция при вступительный экзамен",
            "что такой система прокторинг",
            "мочь ли я сдавать вступительный экзамен из дом",
            "когда становиться известный результат вступительный экзамен",
            "где можно находить демо версия вступительный экзамен",
            "существовать ли инклюзивный сопровождение при сдача вступительный экзамен по материал вуз",
            "мочь ли я получать комната в общежитие на время сдача вступительный экзамен",
            "какой минимальный балл необходимо набирать для участие в конкурс на поступление",
            "какой минимальный балл для обучение по контракт",
            "как подбирать направление с учет сдавать экзамен",
        ],
        [
            "как оценивать свой шанс поступать на бюджет",
            "какой минимальный балл для обучение по контракт",
            "где посмотреть рейтинговый список",
            "какой проходной балл прошлый год",
            "сколько бюджетный место на направление",
            "где посмотреть приказ на зачисление",
            "когда издаваться приказ на зачисление",
            "можно ли пойти на контракт если не поступать на бюджет",
        ],
        [
            "кто иметь право получать комната в общежитие",
            "какой условие правило проживание в общежитие",
            "какой нужный документ для заселение",
            "когда я должный подавать документ для заселение",
            "мочь ли я получать комната в общежитие после поступление",
            "мочь ли я выселяться из комната до окончание обучение",
            "сколько стоить проживание",
            "что входить в стоимость проживание  нужно ли оплачивать коммунальный услуга",
            "как получать комната в общежитие повышенный комфортность",
            "когда происходить заселение в общежитие",
            "мочь ли я заселяться рано поздно общежитие",
            "мочь ли я выселять из общежитие",
            "мочь ли я поменять комната общежитие если я чтото быть не устраивать", 
            "можно ли приводить гость",
            "можно ли держать домашний животное",
            "мочь ли я получать комната на время вступительный экзамен",
        ]
    ]
    return questions

def get_clear_questions():
    questions = [ 
                [
                    "До какого числа нужно подать документы?",
                    "Как подать документы через сайт?",
                    "Как подать документы лично?",
                    "Как подать документы по почте?",
                    "Как подать документы через Госуслуги?",
                    "Как изменить поданное заявление?",
                    "Какие документы нужны для поступления по общему конкурсу?",
                    "Какие документы нужны для целевого приема?",
                    "Какие документы нужны для приема без экзаменов?",
                    "Какие документы нужны для приема вне конкурса (особая квота)?",
                    "Какие документы нужны иностранным гражданам?",
                    "Нужны ли оригиналы?",
                    "Что такое обучение по контракту?",
                    "Где можно взять шаблон договора?",
                    "До какого числа нужно заключить договор?",
                    "Кто и как заключает договор? ",
                    "Как можно оплатить (мат. Капитал, оплата онлайн, образовательный кредит)?",
                    "Где можно взять шаблон согласия?",
                    "До какого числа нужно подать согласие?",
                    "Сколько согласий одновременно можно подать?",
                    "Можно ли менять поданное согласие?",
                    "Как подать согласие?"
                ],
                [
                    "Когда начинается прием документов?",
                    "Когда заканчивается прием документов?",
                    "До какого числа можно вносить изменения в заявление?",
                    "До какого числа необходимо подать согласие ?",
                    "До какого числа можно заключить договор на контрактное обучение?",
                    "До какого числа необходимо предоставить оригиналы?",
                    "Когда публикуются приказы о зачислении?",
                    "Когда проводятся вступительные испытания по материалам ВУЗа?",
                    "Когда станут известны результаты экзаменов?",
                    "Как найти расписание вступительных испытаний?",
                    "Когда проводится апелляция?",
                    "Когда публикуются приказы о зачислении на бюджетные места?",
                    "Когда публикуются приказы о зачислении на контрактные места?",
                    "Когда публикуются приказы о зачислении на места в пределах особой квоты?",
                    "Когда нужно подать документы на заселение?",
                    "Когда будет заселение в общежитие?",
                    "Могу ли я заселиться раньше/позже?"
                ],
                [
                    "Какие «льготы» установлены правилами приема?",
                    "Какие документы подавать при поступлении по «льготе»?",
                    "До какого числа необходимо подать документы «по льготе»?",
                    "Можно ли сдавать вступительные испытания по материалам ВУЗа, если я поступаю по «льготе»?",
                    "Какие минимальные баллы ЕГЭ нужны при поступлении «по льготе»?",
                    "Когда издается приказ о зачислении «по льготе»?",
                    "Есть ли инклюзивное сопровождение при поступлении в НГТУ?",
                    "На какие направления действует «льготное право поступление»? ",
                    "На сколько направлений действует «льготное право поступление»?",
                    "Кто может поступать «без вступительных испытаний»?",
                    "До какого числа необходимо подать документы при поступлении «БВИ»?",
                    "Какие документы подавать при поступлении БВИ?",
                    "Нужно ли иметь результаты ЕГЭ при поступлении БВИ?",
                    "Можно ли воспользоваться правом поступления БВИ, если сдавать вступительные испытания по материалам ВУЗа?",
                    "Когда издается приказ о зачислении «БВИ»?",
                    "На сколько направлений действует право поступление «БВИ»?",
                    "Что такое целевое обучение?",
                    "Кто заключает договор на целевое обучение? (возможно, дублирует после следующий вопрос)",
                    "Где взять шаблон договора на целевое обучение? (возможно, дублирует следующий вопрос)",
                    "Как заключить договор на целевое обучение?",
                    "Какие документы необходимо подавать при поступлении на целевое обучение?",
                    "До какого числа необходимо подать документы при поступлении на целевое обучение?",
                    "Когда издается приказ о зачислении на целевое обучение?",
                    "Какие индивидуальные достижения засчитываются при поступлении?",
                    "Сколько баллов можно получить за индивидуальные достижения?",
                    "До какого числа необходимо предоставить документы, подтверждающие наличие индивидуальных достижений?",
                    "Как предоставить документы, подтверждающие наличие индивидуальных достижений?",
                    "За какие года действуют индивидуальные достижения?"
                ],
                [
                    "Какие направления есть в НГТУ?",
                    "На сколько направлений можно подать документы?",
                    "Как поменять направление?",
                    "Смогу ли я поменять направление после поступления?",
                    "Смогу ли перейти на бюджет, если поступлю на контракт? (не уверен, что этот вопрос сюда)",
                    "До какого числа можно изменить направления в заявлении?",
                    "Сколько бюджетных и контарктых мест на напрвлениях? (прям такой вопрос? Здесь имеется ввиду “сколько бюджетный мест на направлении ХХХ?” ? аналогичный вопрос по 2 следующим вопросам)",
                    "Какая стоимость обучения по контаркту на разных направлениях?",
                    "Какие экзамены нужно сдавать для поступления на различные направления НГТУ?",
                    "Подобрать направление, с учетом сданных экзаменов?"
                ],
                [
                    "Какие минимальные баллы ЕГЭ?",
                    "Какие ЕГЭ нужно сдавать для разных направлений?",
                    "ЕГЭ за какие года действуют?",
                    "Где можно сдать ЕГЭ?",
                    "Кто имеет права сдавать ЕГЭ?",
                    "Нужно ли предоставлять свидетельство с результатами ЕГЭ?",
                    "Если я сдал(а) ЕГЭ, нужно ли мне сдавать ВИ? (возможно, дублирует следующей вопрос)",
                    "Кто имеет право сдавит ВИ?",
                    "Как записаться на сдачу ВИ?",
                    "До какого числа необходимо подать документы при поступлении по ВИ?",
                    "Где будет происходить сдача ВИ?",
                    "В каком формате проходят ВИ?",
                    "В какие даты проходят ВИ (расписание)?",
                    "Как проходит апелляция при ВИ?",
                    "Что такое система «прокторинга»?",
                    "Могу ли я сдать ВИ из дома?",
                    "Когда станут известны результаты ВИ?",
                    "Где можно найти демоверсии ВИ?",
                    "Существует ли инклюзивное сопровождении при сдачи ВИ по материалам ВУЗа?",
                    "Могу ли я получить комнату в общежитии на время сдачи ВИ?",
                    "Какие минимальные баллы необходимо набрать для участия в конкурсе на поступление?",
                    "Какие минимальные баллы для обучения по контракту?",
                    "Подобрать направление, с учетом сданных экзаменов?"
                ],
                [
                    "Как оценить свои шансы поступит на бюджет? (Если бы поступление было сегодня)",
                    "Какие минимальные баллы для обучения по контракту?",
                    "Где просмотреть рейтинговые списки?",
                    "Какие проходные баллы прошлых лет?",
                    "Сколько бюджетные мест на направлениях?",
                    "Где просмотреть приказы на зачисление?",
                    "Когда издаются приказы на зачисления?",
                    "Можно ли пойти на контракт, если не поступил на бюджет?"
                ],
                [
                    "Кто имеет право получить комнату в общежитии?",
                    "Какие условия проживания в общежитии (правила, права и обязанности)?",
                    "Какие нужны документы для заселения?",
                    "Когда я должен подать документы для заселения?",
                    "Могу ли я получить комнату в общежитии после поступления?",
                    "Могу ли я выселиться из комнаты до окончания обучения?",
                    "Сколько стоит проживание?",
                    "Что входит в стоимость проживания? | нужно ли оплачивать коммунальные услуги?",
                    "Как получить комнату в общежитии повышенной комфортности?",
                    "Когда происходит заселение в общежитие?",
                    "Могу ли я заселиться раньше/позже?",
                    "Могут ли меня выселить из общежития?",
                    "Смогу ли я поменять комнату/общежитие, если меня что-то будет не устраивать?",
                    "Можно ли приводить гостей?",
                    "Можно ли держать домашних животных?",
                    "Могу ли я получить комнату на время ВИ?"
                ]
            ]
    return questions



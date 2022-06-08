#Чтение списка ответов из файла
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
    db = []
    iterator = 1
    for i in range(7):
        db.append([])

    f = open("final/baseNew.txt", 'r', encoding="utf-8")
    for line in f:
        if(len(line) == 2):
                iterator = int(line[0])
                continue
        db[iterator - 1].append(line)
    f.close()
    return db

def get_clear_questions():
    db = []
    iterator = 1
    for i in range(7):
        db.append([])

    f = open("final/baseQ.txt", 'r', encoding="utf-8")
    for line in f:
        if(len(line) == 2):
                iterator = int(line[0])
                continue
        db[iterator - 1].append(line)
    f.close()
    return db
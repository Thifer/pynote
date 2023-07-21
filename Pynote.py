from datetime import datetime
import csv

notehead: str
note: str
date: datetime
filename: str
filename = 'note.csv'


def newnote():
    notehead = input("Введите название заметки: ")
    note = input("Введите заметку: ")
    date = datetime.now()
    fullnote = [notehead, note, date]
    writenote(fullnote)


def changenote():
    pass


def findnote():
    pass


def writenote(fullnote: list):
    notes = readnote()
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerows(notes)
        writer.writerow(fullnote)


def readnote():
    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f, delimiter=';')
        return list(reader)


def printnote():
    notes = readnote()
    count = 0
    print("Какую заметку вывести?")
    for row in notes:
        print(f"{(count+1)}. {row[0]}")
        count += 1
    answer = input("Вао ответ: ")
    if(int(answer)>0)&(int(answer)<=count+1):
        print(notes[int(answer)-1][1])

def menu():
    print("Добро пожаловать в меню заметок")
    print("Пожалуйста, выберете действие")
    print("1.Создать заметку")
    print("2.Редактировать заметку")
    print("3.Найти заметку")
    print('4.Прочитать заметку')
    print("Любой другой ввод - для выхода")
    asnwer = int(input("Ответ: "))
    if asnwer == 1:
        newnote()
    elif asnwer == 2:
        changenote()
    elif asnwer == 3:
        findnote()
    elif asnwer == 4:
        printnote()
    else:
        print("Досвидания")


if __name__ == '__main__':
    menu()

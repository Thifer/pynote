from datetime import datetime
import csv

# TODO Приложение должно запускаться без ошибок DONE
# TODO должно уметь сохранять данныев файл DONE
# TODO уметь читать данные из файла, DONE
# TODO делать выборку по дате,
# TODO выводить на экран выбранную запись DONE
# TODO выводить на экран весь список записок DONE
# TODO добавлятьзаписку DONE
# TODO редактировать ее DONE
# TODO удалять.DONE
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


def deletenote():
    notes = readnote()
    count = 0
    print("Какую заметку удалить???")
    for row in notes:
        print(f"{(count + 1)}. {row[0]}")
        count += 1
    answer = int(input("Ваш ответ?: "))
    notes.remove(notes[answer-1])
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerows(notes)



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


def noteedit():
    notes = readnote()
    count = 0
    print("Какую заметку редактировать??")
    for row in notes:
        print(f"{(count + 1)}. {row[0]}")
        count += 1
    answer = int(input("Введите номер: "))
    if answer >= count:
        print("Неверный ввод")
        return
    print("Что будем редактировать?")
    print("1.Имя")
    print("2.Саму заметку")
    secondanswer = int(input("Введите ваш ответ: "))
    if secondanswer-1 >= 2:
        print("Неверный ввод")
        return
    editlist = readnote()
    if secondanswer-1 == 0:
        editlist[answer-1][secondanswer-1] = input("Введите новый текст: ")
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(editlist)

def printallnotes():
    notes = readnote()
    for note in notes:
        print(f"Имя заметки:{note[0]}")
        print(f"Время создания заметки:{note[2]}")
        print(f"Заметка:{note[1]}")
        print("==========")


def printnote():
    notes = readnote()
    count = 0
    print("Какую заметку вывести?")
    for row in notes:
        print(f"{(count + 1)}. {row[0]}")
        count += 1
    answer = input("Вао ответ: ")
    if (int(answer) > 0) & (int(answer) <= count + 1):
        print(notes[int(answer) - 1][1])


def menu():
    print("Добро пожаловать в меню заметок")
    print("Пожалуйста, выберете действие")
    print("1.Создать заметку")
    print("2.Редактировать заметку")
    print('3.Прочитать заметку')
    print("4.Прочитать все заметки")
    print("5.Удалить заметку")
    print("Любой другой ввод - для выхода")
    asnwer = input("Ответ: ")
    if asnwer == "1":
        newnote()
    elif asnwer == "2":
        noteedit()
    elif asnwer == "3":
        printnote()
    elif asnwer == "4":
        printallnotes()
    elif asnwer == "5":
        deletenote()
    else:
        print("Досвидания")


if __name__ == '__main__':
    menu()

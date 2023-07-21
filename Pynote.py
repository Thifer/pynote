from datetime import datetime
import csv

notehead: str
note: str
date: datetime
filename: str
filename = 'note.csv'
notes: list


def newnote():
    notehead = input("Введите название заметки: ")
    note = input("Введите заметку: ")
    date = datetime.now()
    fullnote = [notehead, note, date]
    notes.append(fullnote)


def deletenote():
    count = 0
    print("Какую заметку удалить???")
    for row in notes:
        print(f"{(count + 1)}. {row[0]}")
        count += 1
    answer = int(input("Ваш ответ?: "))
    notes.remove(notes[answer - 1])


def writenote():
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerows(notes)


def readnote():
    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f, delimiter=';')
        return list(reader)


def noteedit():
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
    if secondanswer - 1 >= 2:
        print("Неверный ввод")
        return
    editlist = readnote()
    if secondanswer - 1 == 0:
        editlist[answer - 1][secondanswer - 1] = input("Введите новый текст: ")


def printallnotes():
    for note in notes:
        print(f"Имя заметки:{note[0]}")
        print(f"Время создания заметки:{note[2]}")
        print(f"Заметка:{note[1]}")
        print("==========")


def printnote():
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
    print("exit - для выхода")
    print("Любой другой ввод - для выхода")
    answer = input("Ответ: ")
    if answer == "1":
        newnote()
    elif answer == "2":
        noteedit()
    elif answer == "3":
        printnote()
    elif answer == "4":
        printallnotes()
    elif answer == "5":
        deletenote()
    elif answer == "exit":
        print("Досвидания")
        return
    else:
        menu()


if __name__ == '__main__':
    notes = readnote()
    menu()
    writenote()

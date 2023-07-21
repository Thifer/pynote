from datetime import datetime
import csv

notehead: str
note: str
date: datetime


def newnote():
    pass


def changenote():
    pass


def findnote():
    pass


def menu():
    print("Добро пожаловать в меню заметок")
    print("Пожалуйста, выберете действие")
    print("1.Создать заметку")
    print("2.Редактировать заметку")
    print("3.Найти заметку")
    print("Любой другой ввод - для выхода")
    print()
    asnwer = int(input())
    if asnwer == 1:
        newnote()
    elif asnwer == 2:
        changenote()
    elif asnwer == 3:
        findnote()
    else:
        print("Досвидания")


if __name__ == '__main__':
    menu()

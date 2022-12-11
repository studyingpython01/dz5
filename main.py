import shutil
from victory import questions as que
import random
import platform
import sys
import os
while True:
    print('- создать папку: 1')
    print('- удалить папку: 2')
    print('- копировать папку: 3')
    print('- создать файл: 4')
    print('- удалить файл: 5')
    print('- копировать файл: 6')
    print('- просмотр содержимого рабочей директории: 7')
    print('- посмотреть только папки: 8')
    print('- посмотреть только файлы: 9')
    print('- просмотр информации об операционной системе:10')
    print('- создатель программы: 11')
    print('- играть в викторину`: 12')
    print('- мой банковский счет: 13')
    answer = int(input('Введите цифру:'))
    if answer == 1 :
        answer1 = input('Введите имя папки:')
        os.mkdir(answer1)
    if answer == 2:
        answer2 = input('Введите имя папки:')
        os.rmdir(answer2)
    if answer == 3:
        answer3 = input('Что вы хотите копировать?')
        answer4 = input('Последующее имя папки:')
        shutil.copy(answer3, answer4)
    if answer == 4:
        answer5 = input('Имя файла:')
        file = open(answer5, 'w+')
        file.close()
    if answer == 5:
        my_answer2 = input('Введите имя файла:')
        os.remove(my_answer2)
    if answer == 6:
      my_answer = input('Какой файл вы хотите скопировать?')
      my_answer1 = input(' В какой файл ?')
      shutil.copy(my_answer, my_answer1)
    if answer == 7:
       print(os.listdir(path="."))
    if answer == 8:
        folders = []
        for filename in os.listdir():
            m_answer = os.path.isdir(filename)
            print(m_answer)
            if m_answer == False:
               folders.append(filename)
               print(folders)
    if answer == 9:
        files = []
        for filename in os.listdir():
            m_answer1 = os.path.isfile(filename)
        if m_answer1 == True:
            files.append(filename)
        print(files)
    if answer == 10:
        print(os.uname())
    if answer == 11:
        print('Сделано Васильевым Артёмом (12 лет)')
    if answer == 12:
        que()

    if answer == 13:
        card = 0
        buyings = []
        print('На вашем счету', card, 'рублей.')
        money = []
        while True:
            print('Вы можете:')
            print('1. Пополнить свой счёт;')
            print('2. Что-либо купить;')
            print('3. Просмотреть историю покупок;')
            print('4. Выйти из программы.')
            choice = input('Выберите пункт меню')
            if choice == '1':
                money_in = int(input('Сколько денег вы хотите положить на свой счёт?'))
                card += money_in
                print('Перевод средств осуществлён.')
                pass
            elif choice == '2':
                answer_d = int(input('Сколько денег вы хотите потратить?'))
                if answer_d > card:
                    print('К сожалению, на вашем счёте недостаточно денег.')
                    pass
                else:
                    answer_c = input('Вы совершили покупку. Пожалуйста, назовите её.')
                    card -= answer_d
                    buyings.append(answer_c, answer_d)
                pass
            elif choice == '3':
                print('Ваш лист покупок:', list(buyings))
                pass
            elif choice == '4':
                break
            else:
                print('Неверный пункт меню')

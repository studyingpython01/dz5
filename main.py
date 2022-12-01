import shutil
import random
  # False
x = 8
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
         something = 0
    if answer == 11:
        print('Сделано Васильевым Артёмом (12 лет)')
    if answer == 12:
        while True:

            birthdays = {'napoleon': '15.08.1769',
                         'zuckerberg': '14.05.1984',
                         'musk': '28.06.1971',
                         'bezos': '12.01.1964',
                         'da_vinci': '02.04.1452',
                         'newton': '04.01.1643',
                         'einstein': '14.03.1879',
                         'columbus': '31.10.1451',
                         'paster': '27.12.1822',
                         'darwin': '12.02.1809'
                         }
            answers = {
                '15.08.1769': 'Пятнадцатое августа 1769 года',
                '14.05.1984': 'Четырнадцатое мая 1984 года',
                '28.06.1971': 'Двадцать восьмое июня 1971 года',
                '12.01.1964': 'Двенадцатое января 1964 года',
                '02.04.1452': 'Второе апреля 1452 года',
                '04.01.1643': 'Четвёртое января 1643 года',
                '14.03.1879': 'Четырнадцатое марта 1879 года',
                '31.10.1451': ' Тридцать первое октября 1451 года',
                '27.12.1822': 'Двадцать седьмое декабря 1822 года',
                '12.02.1809': 'Двенадцатое февраля'
            }
            mistakes = 0
            right = 0

            keys = random.sample(list(birthdays), 5)
            for key in list(keys):
                answer_m = input('Укажите дату рождения(dd.mm.yyyy): ' + key + '\n')
                if answer_m != birthdays[key]:
                    mistakes += 1
                    print(answers.get(birthdays[key]))
                else:
                    right += 1


            def calculate(x, y, z):
                result = x * (y / z)
                return result


            print('Ошибки:', mistakes)
            print('Правильные ответы:', right)
            right = int(right)
            mistakes = int(mistakes)
            print('Процент правильных ответов:', calculate(right, 100, 5))
            print('Процент неправильных ответов:', calculate(mistakes, 100, 5))
            answer_last = input("Хотите начать игру с начала? Если нет, введите 'нет'. Если да, введите 'да'.")
            if answer_last == 'нет':
                break
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
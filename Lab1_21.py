from statistics import *
from random import randint

print('Приветствуем вас в нашей программе. Какую математическую функцию вы хотите использовать?\n'
      'Если вы хотите использовать функцию нахождения максимума/минимума или найти среднееарифметическое выберите режим basic.\n'
      'Если хотите добавить поиск медианы или моды выберите режим advanced.\n'
      'Если хотите добавить поиск среднего геометрического или среднее гармоническое выберите режим scientific.')

'''    P.S. Если вы не понимаете, как писать слово, скопируйте его'''

menu = '''Этот режим может сделать следующее:
1. Найти максимум из списка элементов.
2. Найти минимум из списка элементов.
3. Найти среднее арифметическое списка элементов.'''
menu1 = '''4. Найти медиану списка элементов.
5. Найти моду списка элементов.'''
menu2 = '''6. Найти среднее геометрическое списка элементов.
7. Найти среднее гармоническое списка элементов.'''


def stats_calculator(args, mode1 = 'basic'):
    if mode1 == 'basic':
        print(f'''{menu}
Выберите интересующий вас пункт''')
        choise = input()

        if choise == '1':
            print(max(args))
        elif choise == '2':
            print(min(args))
        elif choise == '3':
            print(sum(args)/len(args))
        else:
            print('Число введено неправильно. Пожалуйста проверьте введённое число')

    elif mode1 == 'advanced':
        print(f'''{menu}\n{menu1}
Выберите интересующий вас пункт''')
        choise = input()

        if choise == '1':
            print(max(args))
        elif choise == '2':
            print(min(args))
        elif choise == '3':
            print(sum(args) / len(args))
        elif choise == '4':
            print(median(args))
        elif choise == '5':
            print(mode(args))
        else:
            print('Число введено неправильно. Пожалуйста проверьте введённое число')

    elif mode1 == 'scientific':
        print(f'''{menu}\n{menu1}\n{menu2}
Выберите интересующий вас пункт''')
        choise = input()

        if choise == '1':
            print(max(args))
        elif choise == '2':
            print(min(args))
        elif choise == '3':
            print(sum(args) / len(args))
        elif choise == '4':
            print(median(args))
        elif choise == '5':
            print(mode(args))
        elif choise == '6':
            print(geometric_mean(args))
        elif choise == '7':
            print(harmonic_mean(args))
        else:
            print('Число введено неправильно. Пожалуйста проверьте введённое число')

mode1 = input().strip().lower() # убирает лишние пробелы в начале и конце введённых строк
n = int(input('Сколько случайно сгенерированных чисел вы хотите проверить?\n'))
nums = [randint(0, 10000) for _ in range(n)]

stats_calculator(nums, mode1)
from statistics import *
from random import randint

menu = '''Какую функцию вы хотите использовать?
1. Максимум.
2. Минимум.
3. Среднее арифметическое.\n'''
menu1 = '''4. Медиану.
5. Моду.\n'''
menu2 = '''6. Среднее геометрическое.
7. Среднее гармоническое.\n'''


def basic(nums, func):
    if func == '1':
        return max(nums)
    elif func == '2':
        return min(nums)
    elif func == '3':
        return fmean(nums)
    return 'Проверьте правильность введённого пункта'


def advanced(nums, func):
    if func in ['1', '2', '3']:
        return basic(nums, func)
    elif func == '4':
        return median(nums)
    elif func == '5':
        return mode(nums)
    return 'Проверьте правильность введённого пункта'


def scientific(nums, func):
    if func in ['1', '2', '3', '4', '5']:
        return advanced(nums, func)
    elif func == '6':
        return geometric_mean(nums)
    elif func == '7':
        return harmonic_mean(nums)
    return 'Проверьте правильность введённого пункта'


def stats_calculator(args, moode):
    if moode == 'basic':
        n = input(f'{menu}')
        return basic(args, n)

    elif moode == 'advanced':
        n = input(f'{menu}{menu1}')
        return advanced(args, n)

    elif moode == 'scientific':
        n = input(f'{menu}{menu1}{menu2}')
        return scientific(args, n)
    else:
        n = input(f'{menu}')
        return basic(args, n)


print('basic ищет максимум, минимум или среднее арифметическое.\n'
      'advanced ищет всё, что и basic, а так же медиану и моду.\n'
      'scientific ищет всё, что и advanced, а так же среднее геометрическое '
      'и среднее гармоническое.')
mode1 = input('Введите режим работы калькулятора '
              '(basic/advanced/scientific):\n').strip().lower()
n = int(input('Сколько случайно сгенерированных чисел вы хотите проверить?\n'
              'Введите целое число.\n'))
start, finish = map(int, input('Введите диапазон целых чисел, '
                               'которые будут сгенерированы.\n'
                               'Сначала введите начало диапазона, затем конец\n'
                               'Числа необходимо ввести через пробел:\n').split())
nums = [randint(start, finish) for _ in range(n)]

print(f'Ваш ответ: {stats_calculator(nums, mode1)}')

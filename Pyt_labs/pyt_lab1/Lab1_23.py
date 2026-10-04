from calendar import month_name
from statistics import *
from random import randint


def basic(nums):
    max_n = max(nums)
    min_n = min(nums)
    midl = fmean(nums)
    return [max_n, min_n, midl]


def advanced(nums):
    max_n, min_n, midl = basic(nums)
    med = median(nums)
    try:
        mod = multimode(nums)
    except (ValueError, StatisticsError):
        mod = None
    if len(mod) > 1:
        mod = None
    return [max_n, min_n, midl, med, mod]


def scientific(nums):
    max_n, min_n, midl, med, mod = advanced(nums)
    try:
        geom = geometric_mean(nums)
        harm = harmonic_mean(nums)
    except (ValueError, StatisticsError):
        geom = None
        harm = None
    return [max_n, min_n, midl, med, mod, geom, harm]


def stats_calculator(args, moode='basic'):
    if moode == 'basic':
        return basic(args)
    elif moode == 'advanced':
        return advanced(args)
    elif moode == 'scientific':
        return scientific(args)
    else:
        return basic(args)


print('basic ищет максимум, минимум и среднее арифметическое.\n'
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
nums = [randint(min(start, finish), max(start, finish)) for _ in range(n)]

# print(f'Ваш ответ: {stats_calculator(nums, mode1)}')

if mode1 in ['basic', "advanced", "scientific"]:
    print(f"Максимум: {stats_calculator(nums, mode1)[0]}")
    print(f"Минимум: {stats_calculator(nums, mode1)[1]}")
    print(f"Среднее арифметическое: {stats_calculator(nums, mode1)[2]}")
    if mode1 in ["advanced", "scientific"]:
        print(f"Медиана: {stats_calculator(nums, mode1)[3]}")
        print(f"Мода: {stats_calculator(nums, mode1)[4]}")
        if mode1 == "scientific":
            print(
                f"Среднее геометрическое: {stats_calculator(nums, mode1)[5]}")
            print(f"Среднее гармоническое: {stats_calculator(nums, mode1)[6]}")

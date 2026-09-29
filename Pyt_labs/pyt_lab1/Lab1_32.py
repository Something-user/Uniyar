from random import randint
from datetime import date


def beautiful_dates(dates):
    form_date = list()
    for date2 in dates:
        form_date.append(date2.strftime("%d-%m-%Y"))
    return form_date


def future(dates):
    future_dates = list()
    today = date.today()
    for date1 in dates:
        if today < date1:
            future_dates.append(date1)
    return future_dates


def check_dates(dates):
    correct_dates = list()
    uncor_dates = list()

    for i in range(len(dates)):
        day, month, year = list(map(int, dates[i].split('.')))

        try:
            date1 = date(year, month, day)
            correct_dates.append(date1)
        except ValueError:
            uncor_dates.append(f"{day}-{month}-{year}")

    return correct_dates


dates = list()
while True:
    try:
        n = int(input('Введите количество дат: \n'))
        if n > 0:
            break
        else:
            print("Введите положительное число")
    except ValueError:
        print("Введите целое число!")

while True:
    try:
        day_down, day_high = map(int, input('Введите границы '
                                            'генерации дня: \n').split())
        month_down, month_high = map(int, input('Введите границы '
                                                'генерации месяца: \n').split())
        year_high, year_down = map(int, input('Введите границы '
                                              'генерации года: \n').split())
        break
    except ValueError:
        print("Введите целые числа через пробел!")

for _ in range(n):
    day = randint(min(day_down, day_high), max(day_down, day_high))
    month = randint(min(month_down, month_high), max(month_down, month_high))
    year = randint(min(year_down, year_high), max(year_down, year_high))

    dates.append(f"{day}.{month}.{year}")

core_date = check_dates(dates)
fut_date = future(core_date)

corect_date = beautiful_dates(core_date)
future_date = beautiful_dates(fut_date)

print(f"Корректные даты: {corect_date} \n"
      f"Количество корректных дат: {len(core_date)} \n"
      f"Самая ранняя дата: {min(core_date).strftime('%d-%m-%Y')} \n"
      f"Самая поздняя дата: {max(core_date).strftime('%d-%m-%Y')} \n"
      f"Будущие даты: {future_date}")

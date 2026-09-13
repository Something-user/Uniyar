from random import randint

def lyear(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def zeros(zday, zmonth):
    num1 = str(zday).zfill(2)
    num2 = str(zmonth).zfill(2)
    return [num1, num2]

def chek_dates(dates):
    ansdate = list()
    for i in range(len(dates)):
        day, month, year = list(map(int, dates[i].split('.')))

        if not lyear(year) and month == 2 and day > 28:
            day, month = zeros(day, month)
            ansdate.append(f'{day}.{month}.{year} Ошибка даты')
        elif lyear(year) and month == 2 and day > 29:
            day, month = zeros(day, month)
            ansdate.append(f'{day}.{month}.{year} Ошибка даты')
        elif month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
            day, month = zeros(day, month)
            ansdate.append(f'{day}.{month}.{year} Ошибка даты')
        elif month in [4, 6, 11, 9] and day > 30:
            day, month = zeros(day, month)
            ansdate.append(f'{day}.{month}.{year} Ошибка даты')
        else:
            day, month = zeros(day, month)
            ansdate.append(f"{day}.{month}.{year} Дата верна")

    return ansdate

dates = list()
n = int(input('Введите количество дат, которые хотите сгенерировать: \n'))

for _ in range(n):
    day = randint(1, 31)
    month = randint(1, 12)
    year = randint(1, 10000)
    dates.append(f"{day}.{month}.{year}")

print(chek_dates(dates))
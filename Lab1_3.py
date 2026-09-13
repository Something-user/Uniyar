def lyear(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def chek_dates(dates):
    ansdate = list()

    for i in range(len(dates)):
        day, month, year = list(map(int, dates[i].split('.')))
        if 12 < month or month < 1:
            ansdate.append(f'Ошибка даты  номер {i+1}')

        elif not lyear(year) and month == 2 and day > 28:
            ansdate.append(f'Ошибка даты  номер {i + 1}')

        elif lyear(year) and month == 2 and day > 29:
            ansdate.append(f'Ошибка даты  номер {i+1}')

        elif month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
            ansdate.append(f'Ошибка даты  номер {i+1}')

        elif month in [4, 6, 11, 9] and day > 30:
            ansdate.append(f'Ошибка даты  номер {i+1}')
        else:
            ansdate.append(f"{day}.{month}.{year}")

    return ansdate

n = int(input('Введите количество дат, которые хотите ввести: '))
print('Вводите даты по одной в строчку. После каждой введённой даты нужно нажать Enter. '
      'Даты должны быть в формате ДД.ММ.ГГГГ')

dates = list()

for _ in range(n):
    date = input()
    dates.append(date)

print(chek_dates(dates))
from math import sqrt


def calc(a, b, c):
    if a == 0:
        return "Это линейное уравнение"

    d = b ** 2 - 4 * a * c
    if d < 0:
        return "Данное уравнение не имеет решений"
    elif d == 0:
        x = -b / (2 * a)
        return [x]
    else:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return [x1, x2]


while True:
    try:
        a, b, c = map(float, input('Введите коэффициенты a, b, c '
                                   'через пробел: \n').split())
        break
    except ValueError:
        print("Введите числа")

if len(calc(a, b, c)) == 2:
    print(f"x1 = {calc(a, b, c)[0]}, x2 = {calc(a, b, c)[1]}")
elif len(calc(a, b, c)) == 1:
    print(f"x = {calc(a, b, c)[0]}")
else:
    print(calc(a, b, c))

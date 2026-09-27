from math import sqrt

def calc(a, b, c):
    if a == 0:
        x0 = -c / b
        return f"Это линейное уравнение. Оно имеет один корень: {x0}"

    d = b ** 2 - 4 * a * c
    if d < 0:
        return "Данное уравнение не имеет решений"
    elif d == 0:
        x = -b / (2 * a)
        return f"Ответ: x = {x}"
    else:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return f"Ответ: x1 = {x1}, x2 = {x2}"

while True:
    try:
        a, b, c = map(float, input('Введите коэффициенты a, b, c '
                                   'через пробел: \n').split())
        break
    except ValueError:
        print("Введите числа")

print(calc(a, b, c))
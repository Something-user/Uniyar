from math import *

a, b, c = map(float, input('Введите коэффициенты a, b, c через пробел: \n').split())

d = b ** 2 - 4 * a * c
if d < 0:
    print("Данное уравнение не имеет решений")
elif d == 0:
    x = -b / (2 * a)
    print(f"Ответ: x = {x}")
else:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(f"Ответ: x1 = {x1}, x2 = {x2}")
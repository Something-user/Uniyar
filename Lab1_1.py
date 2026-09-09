from math import *

a, b, c = map(int, input().split())

d = b ** 2 - 4 * a * c
if d < 0:
    print("Данное уравнение не имеет решений")
elif d == 0:
    x = -b / (2 * a)
    print("Ответ: x = {}".format(x))
else:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print("Ответ: x1 = {0}, x2 = {1}".format(x1, x2))
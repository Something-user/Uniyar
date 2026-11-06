import re
from functools import reduce

def correct_string(data):
    cor_purchas = list()
    counter_uncorrect = 0
    for s in data:
        if re.fullmatch(pattern, s):
            cor_purchas.append(s.rsplit(' --- ', maxsplit=1))
        else:
            counter_uncorrect += 1
    return [counter_uncorrect, cor_purchas]


data = list()
while True:
    try:
        N = int(input('Введите количество покупок:\n'))
        if N <= 0:
            print("Число должно быть больше нуля!")
        else:
            break
    except ValueError:
        print("Введите целое число!")
print("Каждая покупка должна иметь вид 'товар --- цена руб коп.'")
for _ in range(N):
    string = input("Введите покупку вида:\n").strip()
    data.append(string)

pattern = r'^(\S(?:.*\S)?) --- (\d+)(?:,(\d{2}))? (руб|коп)\.?$'

counter, purchases = correct_string(data)

pat_digit = r'\d+(?:[.,]\d+)?'
data_output = [
    [x[0], float(re.search(pat_digit, x[1].replace(',', '.')).group())] for x
    in purchases]
data_output.sort(key=lambda x: x[1])
output = [x[0] + ': ' + str(x[1]) for x in data_output if x[1] >= 1000.00]

summa = reduce(lambda a, x: a + x[1], data_output, 0)

print()
print("Вывод:")
for x in output:
    print(x)
print()
print(f"Итого: {summa:.2f}")
print(f"Некорректных строк: {counter}")

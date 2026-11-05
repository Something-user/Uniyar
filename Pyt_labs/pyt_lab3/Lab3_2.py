import re


def summa_purchase(data):
    summa = 0
    for x in data:
        summa += x[1]
    return summa


def correct_string(data):
    cor_purches = list()
    counter_uncorrect = 0
    for s in data:
        if re.fullmatch(pattern, s):
            cor_purches.append(s.rsplit(' --- ', maxsplit=1))
        else:
            counter_uncorrect += 1
    return [counter_uncorrect, cor_purches]


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
pat_digit = r'[-+]?\d+(?:[.,]\d+)?'

counter, purchases = correct_string(data)

data_output = [
    [x[0], float(re.search(pat_digit, x[1].replace(',', '.')).group())] for x
    in purchases]
data_output.sort(key=lambda x: x[1])
output = [x[0] + ': ' + str(x[1]) for x in data_output if x[1] >= 1000]

print()
print("Вывод:")
for x in output:
    print(x)
print()
print(f"Итого: {summa_purchase(data_output):.2f}")
print(f"Некорректных строк: {counter}")

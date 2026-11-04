import re


def rsplit_re(ans):
    output = list()
    for s in ans:
        string = re.split(' --- ', s, maxsplit=0)
        ans_s = string[0]
        for i in range(1, len(string) - 1):
            ans_s = ans_s + ' --- ' + string[i]
        output.append([ans_s, float((re.search(pat_digit, string[-1])).group().replace(',', '.'))])
    return output

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

for _ in range(N):
    string = input("Введите покупку вида 'название --- цена':\n").strip()
    data.append(string)

pattern = r'^(\S(?:.*\S)?) --- (\d+)(?:,(\d{2}))? (руб|коп)\.?$'
pat_digit = r'[-+]?\d+(?:[.,]\d+)?'

print(data)

ans = list()
counter = 0
for s in data:
    if re.fullmatch(pattern, s):
        ans.append(s)
    else:
        counter += 1

print(ans)
print(counter)

answers = list()
for s in ans:
    string = s.split(' --- ')
    print(string)

print(rsplit_re(ans))

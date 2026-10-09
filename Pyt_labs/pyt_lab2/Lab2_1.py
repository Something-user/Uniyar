from random import randint

while True:
    try:
        M = int(input("Введите размеры матрицы: "))
        break
    except ValueError:
        print("Введите ЧИСЛО!")

ans = []

lst = []
for _ in range(M):
    row = [0 for _ in range(M)]
    lst.append(row)

while True:
    for i in range(M):
        for j in range(M):
            lst[i][j] = randint(-100, 100)

    for x in range(M):
        print(lst[x])

    lst1 = []
    for i in range(M):
        row1 = []
        for j in range(M):
            row1.append(lst[j][i])
        lst1.append(row1)

    for i in range(M):
        tmp = []
        for j in range(M):
            mini = min(lst[i])
            if lst[i][j] == mini:
                tmp.append([lst[i][j], i, j])
        for h in tmp:
            n, m = h[1:]
            if h[0] == max(lst1[m]):
                ans.append(h)

    if len(ans):
        print(ans)
        break
    else:
        print("Седловые точки не найдены")
        print()

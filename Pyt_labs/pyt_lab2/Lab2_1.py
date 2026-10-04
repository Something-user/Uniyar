from random import randint, seed

M = int(input())
seed(87)
lst = []
for _ in range(M):
    row = [0 for _ in range(M)]
    lst.append(row)
for i in range(M):
    for j in range(M):
        lst[i][j] = randint(10, 99)


for x in range(M):
    print(*lst[x])

maximum1 = list()
for k in range(M):
    maximum = -10000
    max_elem = list()
    for j in range(M):
        if lst[j][k] > maximum:
            maximum = lst[j][k]
    maximum1.append(maximum)


print()
print(maximum1)
from random import randint, seed
from math import inf

M = 4
ans = []
'''
seed(87)
lst = []
for _ in range(M):
    row = [0 for _ in range(M)]
    lst.append(row)

for i in range(M):
    for j in range(M):
        lst[i][j] = randint(10, 99)
'''
lst = [
    [9,  6, (3), (3)],
    [9,  5,   1,   0],
    [9,  6, (3), (3)],
    [9,  5,   0,   2],
]
for x in range(M):
    print(*lst[x])

print()
print()

lst1 = []
for i in range(M):
    row1 = []
    for j in range(M):
        row1.append(lst[j][i])
    lst1.append(row1)

for x in range(M):
    print(*lst1[x])

"""
maximum1 = list()
ans = []
for k in range(M):
    maximum = -10000
    for t in range(M):
        if lst[t][k] > maximum:
            maximum = lst[t][k]
    maximum1.append(maximum)


print()
print(maximum1)

for i in range(M):
    mini = inf
    for j in range(M):
        if lst[i][j] < mini:
            mini = lst[i][j]"""



'''
for i in range(M):
    mini = [inf, 0, 0]
    for j in range(M):
        if lst[i][j] <= mini[0]:
            mini = [lst[i][j], i, j]

    k, m = mini[1:]
    print(k, m)
    if max(lst1[m]) == mini[0]:
        ans.append(mini)

print(ans)
'''

for i in range(M):
    tmp = []
    for j in range(M):
        print(f"Номер строки {i}")
        mini = min(lst[i])
        if lst[i][j] == mini:
            tmp.append([lst[i][j], i, j])
        print(tmp)
    for k in range(len(tmp)):
        h = tmp[k]
        n, m = h[1:]
        if h[0] == max(lst1[m]):
            ans.append(tmp[k])
    print(f"Промежуточный ответ {ans}")
print(ans)

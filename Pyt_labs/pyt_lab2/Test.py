from random import randint, seed
from math import inf



M = 6
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
    [8, 6, 3, 5, 7, 9],
    [7, 5, 2, 4, 6, 8],
    [9, 7, 4, 6, 8, 10],
    [6, 4, 1, 3, 5, 7],
    [10, 8, 0, 7, 9, 11],
    [5, 3, -1, 2, 4, 6],
]
for x in range(M):
    print(*lst[x])



print()
print()



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


lst1 = []
for i in range(M):
    row1 = []
    for j in range(M):
        row1.append(lst[j][i])
    lst1.append(row1)

for x in range(M):
    print(*lst1[x])

for i in range(M):
    mini = [inf, 0, 0]
    maxi = -1000
    for j in range(M):
        if lst[i][j] < mini[0]:
            mini = [lst[i][j], i, j]

    k, m = mini[1:]
    print(k, m)
    if max(lst1[m]) == mini[0]:
        ans.append(mini)
    # for k in range(M):
    #     if lst[i][k] > maxi:
    #         maxi = lst1[i][k]

print(ans)

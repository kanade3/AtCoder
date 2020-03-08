import math
import itertools

n = int(input())
na = [i for i in range(n)]
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

cntnum = 0
tmp = []
for i, j in itertools.product(na, na):
    if i != j:
        cntnum += 1
        cntwa = 0
        # print(i, j)
        cntwa += ((a[i][0] - a[j][0]) ** 2 + (a[i][1] - a[j][1]) ** 2) ** 0.5
        # print(cntwa)
        tmp.append(cntwa)
print(sum(tmp)/n)

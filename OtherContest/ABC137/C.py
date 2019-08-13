from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


n = int(input())
a = [''.join(sorted(input())) for _ in range(n)]
a.sort()
cnt = 0

# print(a)
cntsub = 1
for i in range(len(a) - 1):
    if a[i] == a[i + 1]:
        cntsub += 1
    elif cntsub > 1:
        # print(cntsub)
        cnt += int(cmb(cntsub, 2))
        cntsub = 1

if cntsub > 1:
    # print(cntsub)
    cnt += int(cmb(cntsub, 2))
print(cnt)

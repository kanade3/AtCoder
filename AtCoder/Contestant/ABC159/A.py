from operator import mul
from functools import reduce


def cmb(n_cmb, r_cmb):
    r_cmb = min(n_cmb - r_cmb, r_cmb)
    if r_cmb == 0: return 1
    over = reduce(mul, range(n_cmb, n_cmb - r_cmb, -1))
    under = reduce(mul, range(1, r_cmb + 1))
    return over // under


n, m = map(int, input().split())

if n <= 1:
    ansn = 0
else:
    ansn = cmb(n, 2)

if m <= 1:
    ansm = 0
else:
    ansm = cmb(m, 2)
print(ansn + ansm)

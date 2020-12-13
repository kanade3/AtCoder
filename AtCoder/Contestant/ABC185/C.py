from operator import mul
from functools import reduce


def cmb(n_cmb, r_cmb):
    r_cmb = min(n_cmb - r_cmb, r_cmb)
    if r_cmb == 0: return 1
    over = reduce(mul, range(n_cmb, n_cmb - r_cmb, -1))
    under = reduce(mul, range(1, r_cmb + 1))
    return over // under


L = int(input())
print(cmb((L - 12) + 11, 11))

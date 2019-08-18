from operator import mul
from functools import reduce


def cmb(n_cmb, r_cmb):
    if n_cmb == 0: return 0
    r_cmb = min(n_cmb - r_cmb, r_cmb)
    if r_cmb == 0: return 1
    over = reduce(mul, range(n_cmb, n_cmb - r_cmb, -1))
    under = reduce(mul, range(1, r_cmb + 1))
    return over // under


n = int(input())
s = [input() for _ in range(n)]
wflag = [0] * 5

for i in s:
    if i[0] == 'M':
        wflag[0] += 1
    elif i[0] == 'A':
        wflag[1] += 1
    elif i[0] == 'R':
        wflag[2] += 1
    elif i[0] == 'C':
        wflag[3] += 1
    elif i[0] == 'H':
        wflag[4] += 1
print(wflag)

in_n = 0
w = 1
for i in wflag:
    if i != 0:
        in_n += 1
        w *= i
print(cmb(in_n, 3) * w)

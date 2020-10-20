from collections import Counter


def in_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default


while (1):
    n, p = map(int, input().split())
    if n == 0 and p == 0:
        exit()
    pot = p

    c = [0] * n

    index = 0
    while (1):
        if pot == 0:
            if in_index(c, p):
                for i in range(n):
                    if c[i] != 0:
                        print(i)
                break
        if pot:
            pot -= 1
            c[index] += 1
        else:
            pot += c[index]
            c[index] = 0
        index += 1
        if index > n - 1:
            index = 0

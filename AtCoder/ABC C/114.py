n = int(input())


def d(s):
    if int(s) > n:
        return 0
    else:
        out = 1 if all(s.count(i) > 0 for i in '753') else 0

        for z in '753':
            out += d(s + z)

        return out


print(d('0'))

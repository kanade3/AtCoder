n = int(input())


def d(a):
    if int(a) > n:
        return 0
    # 初期化
    out = 1 if all(a.count(i) > 0 for i in '753') else 0

    for i in '753':
        out += d(a + i)

    return out


print(d('0'))

memo = {}
a, b, c = map(int, input().split())


def rec(x, y, z):
    # 計算済みならその結果を返す
    if (x, y, z) in memo.keys():
        return memo[(x, y, z)]

    # 計算済みではない新規

    else:
        if x <= y:
            memo[(x, y, z)] = y
            return y
        else:
            r = rec(rec(x - 1, y, z), rec(y - 1, z, x), rec(z - 1, x, y))
            memo[(x, y, z)] = r
            return r


print(rec(a, b, c))
print(memo)
# print(memo[(2, 3, 4)])

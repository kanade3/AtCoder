n, m = map(int, input().split())

cnt = 1
# 約数全列挙する感じで。しないとコーナーケースにかかってしまった。
for i in range(1, int(m ** 0.5) + 1):
    if m % i == 0:
        b = m // i
        if i * n <= m:
            cnt = max(cnt, i)
        if b * n <= m:
            cnt = max(cnt, b)
print(cnt)

# x*y=mを求める。　xを大にしたい。ただしyはn以上。

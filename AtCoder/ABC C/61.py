n, k = map(int, input().split())
c = {}
for i in range(n):
    a, b = map(int, input().split())
    if a in c.keys():
        c.update({a: c[a] + b})
    else:
        c[a] = b
# print(c)


# 順番が保持されないので、辞書のkeyをリストに変換&ソートすることで順番を維持できる。
cnt = 0
for i in sorted(list(c.keys())):
    cnt += c[i]
    if cnt >= k:
        print(i)
        exit()

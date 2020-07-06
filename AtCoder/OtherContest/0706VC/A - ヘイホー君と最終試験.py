n, k, m, r = map(int, input().split())
a = []
for i in range(n):
    if i != n - 1:
        a.append(int(input()))
    else:
        a.append(0)

a = sorted(a, reverse=True)
need = r * k
tmp = sum(a[:k])

if tmp >= need:
    print(0)
    exit()

tmp -= a[k - 1]

ans = max(0, need - tmp)
print(ans if ans <= m else -1)

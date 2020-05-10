n, m, x = map(int, input().split())
master = []
ans = 10 ** 18
for i in range(n):
    b = list(map(int, input().split()))
    master.append(b)

for i in range(2 ** n):
    kau = [0 for _ in range(m + 1)]
    for j in range(n):
        if (i >> j) & 1:
            # print(i)
            for k in range(m + 1):
                kau[k] += master[j][k]
    ng = 0
    for k in range(1, m + 1):
        if kau[k] < x:
            ng = 1
    if not ng:
        ans = min(ans, kau[0])
    # print(ans)
    # print(kau)
print(ans if ans != 10 ** 18 else -1)

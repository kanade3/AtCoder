import math

n, q = map(int, input().split())
a = list(map(int, input().split()))
s = list(map(int, input().split()))

ruiseki = [0] * (n + 1)

for i in range(n):
    ruiseki[i + 1] = math.gcd(ruiseki[i], a[i])
# print(ruiseki)

for i in s:
    if math.gcd(i, ruiseki[-1]) != 1:
        print(math.gcd(i, ruiseki[-1]))
        continue

    ng = 0
    ok = n
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if math.gcd(ruiseki[mid], i) == 1:
            ok = mid
        else:
            ng = mid
    print(ok)

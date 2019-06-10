import math

n = int(input())
a = list(map(int, input().split()))

l = [0]
r = [0]
m = 0
for i in range(n - 1):
    l.append(math.gcd(l[i], a[i]))
    r.append(math.gcd(r[i], a[n - 1 - i]))

for i in range(n):
    m = max(m, math.gcd(l[i], r[n - 1 - i]))
    print(m)

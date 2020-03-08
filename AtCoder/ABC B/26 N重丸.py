import math

N = int(input())
a = [int(input()) for i in range(N)]
a.sort()
s = 0
for i in range(N):
    if i % 2 == 0:
        s += a[i] ** 2
    else:
        s -= a[i] ** 2
print(abs(s * math.pi))

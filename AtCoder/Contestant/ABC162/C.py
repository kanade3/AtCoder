import math

k = int(input())
cnt = 0
for i in range(1, k + 1):
    for j in range(1, k + 1):
        for n in range(1, k + 1):
            tmp = math.gcd(i, j)
            cnt += math.gcd(tmp, n)
print(cnt)

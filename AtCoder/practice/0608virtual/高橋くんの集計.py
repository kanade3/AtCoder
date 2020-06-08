import math

n = int(input())
a = list(map(int, input().split()))
for i in a:
    if i == 0:
        n -= 1
print(math.ceil(sum(a) / n))

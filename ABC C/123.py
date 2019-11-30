import math

n = int(input())
a = [int(input()) for _ in range(5)]

ans = 4 + math.ceil(n / min(a))
print(ans)
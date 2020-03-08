import math

n, m = map(int, input().split())
w = 10 ** 9 + 7
if n + 1 == m or m + 1 == n:
    print(math.factorial(min(n, m)) ** 2 * max(n, m) % w)
elif n == m:
    print(2 * math.factorial(n) ** 2 % w)
else:
    print(0)

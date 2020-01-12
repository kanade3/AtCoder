n, k, m = map(int, input().split())
t = list(map(int, input().split()))

x = int(n * m - sum(t))
if x < 0:
    x = 0
if x <= k:
    print(x)
else:
    print("-1")

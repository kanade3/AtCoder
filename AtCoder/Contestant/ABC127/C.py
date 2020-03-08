N, M = list(map(int, input().split()))
l = 0
r = 10000000
for i in range(M):
    x, y = map(int, input().split())
    l = max(l, x)
    r = min(r, y)

print(r - l + 1 if l <= r else 0)

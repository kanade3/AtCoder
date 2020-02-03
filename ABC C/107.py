n, k = map(int, input().split())
x = list(map(int, input().split()))
l = 0

ans = 10 ** 18
for r in range(k-1, len(x)):
    ans = min(ans, abs(x[l]) + abs(x[r] - x[l]))
    ans = min(ans, abs(x[r]) + abs(x[r] - x[l]))
    l += 1
print(ans)

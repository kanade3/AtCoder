n, k = map(int, input().split())
a = list(map(int, input().split()))
r = 0
cnt = 0
ans = 0

for i in range(n):
    while cnt < k and r < n:
        cnt += a[r]
        r += 1
    if cnt < k:
        break
    else:
        ans += n - r + 1
        cnt -= a[i]
print(ans)

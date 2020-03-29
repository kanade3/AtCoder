n, k = map(int, input().split())
a = list(map(int, input().split()))
max_kyori = a[0] - 0 + (n - a[-1])
cnt = a[0] - 0 + (n - a[-1])
for i in range(k - 1):
    max_kyori = max(max_kyori, a[i + 1] - a[i])
    cnt += a[i + 1] - a[i]
print(cnt - max_kyori)

import bisect

n = int(input())
L = list(map(int, input().split()))
L.sort()
cnt = 0
for a in range(n - 1):
    for b in range(a + 1, n):
        r = bisect.bisect_left(L, L[a] + L[b])
        l = b + 1
        cnt += r - l
print(cnt)

n = int(input())
h = list(map(int, input().split()))
cnt = 0
c = 0
for i in range(n - 1):
    if h[i] >= h[i + 1]:
        cnt += 1
    else:
        c = max(c, cnt)
        cnt = 0
c = max(c, cnt)
print(c)

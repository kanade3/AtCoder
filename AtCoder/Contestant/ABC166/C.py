cnt = 0
n, m = map(int, input().split())
h = list(map(int, input().split()))

ki = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ki[b].append(a)
    ki[a].append(b)

# print(ki)
for i in range(n):
    m = 0
    if len(ki[i]) == 0:
        cnt += 1
        continue
    for j in ki[i]:
        m = max(m, h[j])
    if h[i] > m:
        # print(i, j, h[i])
        cnt += 1
print(cnt)

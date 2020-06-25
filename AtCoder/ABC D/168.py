from collections import deque

n, m = map(int, input().split())

to = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    to[a].append(b)
    to[b].append(a)

q = deque([1])
dist = [-1] * (n + 1)
# print(to)

while q:
    v = q.popleft()

    for u in to[v]:
        if dist[u] != -1:
            continue
        q.append(u)
        dist[u] = v

print("Yes")
# print(dist)

for i in range(2, n + 1):
    print(dist[i])

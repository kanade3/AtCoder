from collections import deque

n = int(input())
to = [[0] for _ in range(n)]
cost = [[0] for _ in range(n)]
for i in range(n - 1):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)
    cost[a].append(w)
    cost[b].append(w)

q = deque()
q.append(0)
ans = [-1] * n
ans[0] = 0

while len(q):
    v = q.pop()
    for i in range(len(to[v])):
        u = to[v][i]
        w = cost[v][i]

        if ans[u] != -1:
            continue
        ans[u] = (ans[v] + w) % 2
        q.append(u)
for i in range(n):
    print(ans[i])

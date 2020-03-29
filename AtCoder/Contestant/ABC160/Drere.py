from collections import deque

n, x, y = map(int, input().split())

tree = [[] for _ in range(n)]

for i in range(n - 1):
    tree[i].append(i + 1)
    tree[i + 1].append(i)
x -= 1
y -= 1
tree[x].append(y)
tree[y].append(x)

ans = [0] * (n - 1)
# 全頂点からBFSする
for i in range(n-1):
    # 頂点xの距離をdistに格納していく
    dist = [-1] * n
    dist[i] = 0
    q = deque([i])
    while len(q):
        v = q.pop()
        for next_v in tree[v]:
            if dist[next_v] != -1:
                continue
            q.appendleft(next_v)
            dist[next_v] = dist[v] + 1
    for j in range(i+1, n):
        ans[dist[j] - 1] += 1

for i in range(n - 1):
    print(ans[i])

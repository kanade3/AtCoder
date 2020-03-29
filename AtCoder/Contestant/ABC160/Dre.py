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
# BFSを全頂点を始点として考える
# それぞれの頂点での距離を考えるものとしてdistを使う
for i in range(n - 1):
    dist = [-1] * n
    dist[i] = 0
    q = deque([i])
    while len(q):
        v = q.pop()
        for next_v in tree[v]:
            if dist[next_v] != -1:
                continue
            q.append(next_v)
            dist[next_v] = dist[v] + 1

    # 単方向から見れば二重カウントで割る必要がなくなるため、i+1からカウントしている。
    for j in range(i + 1, n):
        ans[dist[j] - 1] += 1

for i in range(n - 1):
    print(ans[i])
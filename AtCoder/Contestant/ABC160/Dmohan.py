from collections import deque

N, X, Y = map(int, input().split())
G = [set() for _ in range(N)]
for i in range(N - 1):
    G[i].add(i + 1)
    G[i + 1].add(i)
G[X - 1].add(Y - 1)
G[Y - 1].add(X - 1)

ans = [0] * (N - 1)
for i in range(N - 1):
    # bfs

    dist = [-1] * N
    dist[i] = 0
    q = deque([i])
    while len(q):
        v = q.pop()
        for nv in G[v]:
            # nvには繋がっている辺の番号が入力される。各辺ごとに長さが入る? 例dist[3] には始点と頂点3の間の距離
            if dist[nv] != -1:
                continue
            q.appendleft(nv)
            dist[nv] = dist[v] + 1

    # そして距離-1を順に追加する
    for j in range(i + 1, N):
        ans[dist[j] - 1] += 1

for i in range(N - 1):
    print(ans[i])

from collections import deque

h, w = map(int, input().split())
m = []
cnt_sharp = 0
for i in range(h):
    tmp = input()
    cnt_sharp += tmp.count('#')
    m.append(tmp)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# print(m)
q = deque([])
seen = [[0 for _ in range(w)] for _ in range(h)]
q.append((0, 0, 0))
road = 0
while q:
    y, x, cnt = q.popleft()
    seen[y][x] = 1
    if y == h - 1 and x == w - 1:
        road = cnt + 1
        break
    for ny, nx in zip(dy, dx):
        if 0 <= y + ny < h and 0 <= x + nx < w:
            if seen[y + ny][x + nx] == 0 and m[y + ny][x + nx] == '.':
                seen[y + ny][x + nx] = 1
                # print(y + ny, x + nx, cnt)
                q.append((y + ny, x + nx, cnt + 1))

if road == 0:
    print(-1)
else:
    print(h * w - road - cnt_sharp)

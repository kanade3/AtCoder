from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
field = []
for i in range(r):
    field.append(list(input()))
sy, sx = sy - 1, sx - 1
gy, gx = gy - 1, gx - 1

q = deque([])
q.append((sy, sx, 0))
seen = [[0 for i in range(c)] for j in range(r)]
seen[sy][sx] = 1
while q:
    y, x, cnt = q.popleft()
    # print(y, x, cnt)
    if y == gy and x == gx:
        print(cnt)
        exit()
    for ny, nx in (y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x):
        if ny < 0 or ny >= r or nx < 0 or nx >= c:
            pass
        elif field[ny][nx] == '.' and seen[ny][nx] == 0:
            seen[ny][nx] = 1
            q.append((ny, nx, cnt + 1))

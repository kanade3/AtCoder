from collections import deque

h, w = map(int, input().split())
field = []

for i in range(h):
    field.append(list(input()))

out = 0
for i in range(h):
    for j in range(w):
        if field[i][j] == '.':
            seen = [[0 for m in range(w)] for n in range(h)]
            seen[i][j] = 1
            q = deque([])
            q.append((i, j, 0))
            while q:
                (y, x, cnt) = q.popleft()
                # print(y,x)
                # print(seen)
                for ny, nx in (y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x):
                    if ny < 0 or ny >= h or nx < 0 or nx >= w:
                        pass
                    elif field[ny][nx] == '.' and seen[ny][nx] == 0:
                        q.append((ny, nx, cnt + 1))
                        seen[ny][nx] = 1

            out = max(out, cnt)
print(out)

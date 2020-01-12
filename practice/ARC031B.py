field = []
for i in range(10):
    field.append(list(input()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
# 全部の陸地マスの数を数える
oc = sum([i.count("o") for i in field])


def dfs(x, y):
    seen.append([x, y])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx > 9 or nx < 0 or ny > 9 or ny < 0:
            pass
        elif [nx, ny] in seen:
            pass
        elif field[ny][nx] == "x":
            pass
        else:
            dfs(nx, ny)


c = 0
for i in range(10):
    for j in range(10):
        if field[i][j] == 'x':
            seen = []
            field[i][j] = "o"
            dfs(j, i)
            # 戻さないとまずい
            field[i][j] = "x"

            if len(seen) == oc + 1:
                print("Yes")
                exit(0)
print("NO")

"""
field = []
for i in range(10):
    field.append(list(input()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
oc = sum([i.count("o") for i in field])


def dfs(x, y):
    seen.append([x, y])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx > 9 or nx < 0 or ny > 9 or ny < 0:
            pass
        elif [nx, ny] in seen:
            pass
        elif field[ny][nx] == "x":
            pass
        else:
            dfs(nx, ny)


c = 0
for i in range(10):
    for j in range(10):
        if field[i][j] == "x":
            seen = []
            field[i][j] = "o"
            dfs(j, i)
            field[i][j] = "x"
            if len(seen) == oc + 1:
                print("YES")
                exit()

print("NO")
"""

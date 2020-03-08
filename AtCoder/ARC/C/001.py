dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(h, w):
    seen[h][w] = 1

    # グリッドの4方向探索
    for i in range(4):
        nh = h + dy[i]
        nw = w + dx[i]

        # 場外アウト
        if nh < 0 or nh >= Hin or nw < 0 or nw >= Win:
            continue
        # 壁アウト
        if a[nh][nw] == '#':
            continue
        # 探索済みか
        if seen[nh][nw]:
            continue

        dfs(nh, nw)


Hin, Win = map(int, input().split())

# 下のようなネストされたリストの作り方は誤り
# https://snakify.org/ja/lessons/two_dimensional_lists_arrays/
# seen = [[0] * Win] * Hin

# 正しくは
seen = [[0] * Win for i in range(Hin)]
a = []
for i in range(Hin):
    a.append(input())

sx, sy, gx, gy = 0, 0, 0, 0
for i in range(Hin):
    for j in range(Win):
        if a[i][j] == 's':
            sy, sx = i, j
        if a[i][j] == 'g':
            gy, gx = i, j

dfs(sy, sx)
# print(seen)
# print(gy, gx)
print('Yes' if seen[gy][gx] else 'No')

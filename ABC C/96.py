h, w = map(int, input().split())
a = []
a.append('.' * (w + 2))
for i in range(h):
    a.append('.' + input() + '.')
a.append('.' * (w + 2))

yx = [[1, 0], [0, 1], [0, -1], [-1, 0]]
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if a[i][j] == '#':
            flag = False
            for k in range(4):
                x = yx[k][0]
                y = yx[k][1]
                if a[i + x][j + y] == '#':
                    flag = 1

            if not flag:
                print('No')
                exit()
print('Yes')

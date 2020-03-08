h, w = map(int, input().split())
a = []
a.append('.' * (w + 2))
for i in range(h):
    a.append('.' + input() + '.')
a.append('.' * (w + 2))

indexX = 1
indexY = 1
direct = 1

now = a[indexY][indexX]
cnt = 0
# print(a)
# print(now)

while now != '.':
    cnt += 1

    if now == "\\":
        if direct == 1:
            direct = 4
        elif direct == 2:
            direct = 3
        elif direct == 3:
            direct = 2
        else:
            direct = 1

    elif now == "/":
        if direct == 1:
            direct = 2
        elif direct == 2:
            direct = 1
        elif direct == 3:
            direct = 4
        else:
            direct = 3

    if direct == 1:
        indexX += 1
    elif direct == 2:
        indexY -= 1
    elif direct == 3:
        indexX -= 1
    elif direct == 4:
        indexY += 1

    # print(indexY, indexX)
    now = a[indexY][indexX]

print(cnt)

n = int(input())
l = []
for i in range(n):
    x, y = map(int, input().split())
    l.append([x, y])

flag = 0
for i in range(n):
    x1 = l[i][0]
    y1 = l[i][1]
    for j in range(i + 1, n):
        if j == n:
            break
        x2 = l[j][0]
        y2 = l[j][1]
        for k in range(j + 1, n):
            x3 = l[k][0]
            y3 = l[k][1]
            if k == n:
                break
            # (Ax * By + Bx * Cy + Cx * Ay) - (Ax * Cy + Bx * Ay + Cx * By)
            ans = (x1 * y2 + x2 * y3 + x3 * y1) - (x1 * y3 + x2 * y1 + x3 * y2)
            # print(ans)
            if ans == 0:
                print('Yes')
                exit()
print('No')

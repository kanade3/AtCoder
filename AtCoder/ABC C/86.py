n = int(input())
for i in range(n):
    t, x, y = map(int, input().split())

    if i == 0:
        if x + y != t:
            print('No')
            exit()
        else:
            bx = x
            by = y
            bt = t
    else:
        d = abs(x - bx) + abs(y - by)
        dt = t - bt
        bx = x
        by = y
        bt = t

        # print(d, dt)
        if d > dt:
            print('No')
            exit()

        elif d % 2 == 1 and dt % 2 == 0:
            print('No')
            exit()
        elif d % 2 == 0 and dt % 2 == 1:
            print('No')
            exit()
print('Yes')

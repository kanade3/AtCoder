while (1):
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        exit()
    a = []
    b = [0] * (n+1)

    for i in range(m):
        a.append(list(map(int, input().split())))

    # print(a)
    for y in range(m):
        for x in range(n):
            b[x] += a[y][x]
    # print(b)
    print(max(b))

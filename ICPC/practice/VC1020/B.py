while (1):
    n, r = map(int, input().split())
    if n == 0 and r == 0:
        exit()

    li = [i for i in range(1, n + 1)]

    for i in range(r):
        p, c = map(int, input().split())

        out = []
        for j in range(c):
            index = n - (p + c - 1)
            out.append(li.pop(index))

        for j in range(c):
            li.append(out[j])

    print(li[-1])

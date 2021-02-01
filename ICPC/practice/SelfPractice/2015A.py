while (1):
    m, nmin, nmax = map(int, input().split())
    if m == 0 and nmin == 0 and nmax == 0:
        exit()
    a = []
    for i in range(m):
        b = int(input())
        a.append(b)
    a = sorted(a, reverse=True)

    ans = 10 ** 9
    ans_index = -1
    for i in range(nmin, nmax + 1):
        gapmax = i
        gapmin = i - 1

        if ans >= a[gapmax] - a[gapmin]:
            ans = a[gapmax] - a[gapmin]
            ans_index = i
        # print(a[gapmax] - a[gapmin])
    print(ans_index)

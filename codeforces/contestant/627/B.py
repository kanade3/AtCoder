n = int(input())

for i in range(n):
    l = int(input())
    a = list(map(int, input().split()))
    k = [[] for _ in range(5100)]
    for j in range(l):
        # print(a[j])
        k[a[j]].append(j)

    ok = 0
    for x in range(5100):
        if len(k[x]) == 0:
            continue
        h = k[x][0]
        for y in range(len(k[x])):
            if abs(h - k[x][y]) > 1:
                ok = 1
    print("YES" if ok else "NO")

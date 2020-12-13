n, m, t = map(int, input().split())
a = []
for i in range(m):
    A, b = map(int, input().split())
    a.append([A, b])

time = 0
ans = n
for i in range(m):
    now = a[i][0] - time
    time = a[i][1]

    ans = ans - now
    if ans <= 0:
        print('No')
        exit()

    ans += (a[i][1] - a[i][0])
    # print(a[i][1], ans)
    if ans >= n:
        ans = n

ans -= t - time

if ans <= 0:
    print('No')
else:
    print('Yes')
    # print(ans)

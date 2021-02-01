# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1608&lang=jp


while (1):
    n = int(input())
    if n == 0:
        exit()
    a = sorted(list(map(int, input().split())))
    ans = 10**9
    for i in range(n - 1):
        if abs(a[i + 1] - a[i]) < ans:
            ans = abs(a[i + 1] - a[i])

    print(ans)

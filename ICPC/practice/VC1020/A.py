# https://onlinejudge.u-aizu.ac.jp/beta/room.html#ojaws20201020/info
while (1):
    n = int(input())
    if n == 0:
        exit()
    a = []
    for i in range(n):
        b = int(input())
        a.append(b)
    a = sorted(a)
    a.pop(0)
    a.pop(-1)
    print(sum(a) // (n - 2))

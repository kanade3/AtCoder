n = int(input())
a = []
n -= 1
for i in range(n):
    N, S, F = map(int, input().split())
    a.append([N, S, F])

for i in range(n + 1):
    cnt = 0
    for j in range(i, n):
        # print(i, j,n)
        if j == i:
            cnt += a[j][1] + a[j][0]
        else:
            if cnt >= a[j][1]:
                amari = cnt % a[j][2]
                cnt += a[j][0] + (a[j][2] - amari if amari != 0 else 0)
            else:
                cnt = a[j][1] + a[j][0]
    print(cnt)

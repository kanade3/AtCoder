N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0
for i in range(N):

    if b[i] <= a[i]:
        cnt += b[i]
    else:
        cnt += a[i]
        # 倒せる数を減らす
        b[i] -= a[i]
        # print(cnt)

        if a[i + 1] >= b[i]:
            cnt += b[i]
            a[i + 1] -= b[i]
        else:
            cnt += a[i+1]
            a[i + 1] = 0
print(cnt)
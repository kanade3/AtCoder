n, d, k = map(int, input().split())
r = []

for i in range(d):
    a, b = map(int, input().split())
    r.append([a, b])

ks = []
for i in range(k):
    kb, kf = map(int, input().split())
    ks.append([kb, kf])

for i in range(k):

    cnt = 0

    if ks[i][0] < ks[i][1]:
        k_now = ks[i][0]
        for j in range(d):
            cnt += 1
            if r[j][0] <= k_now <= r[j][1]:
                k_now = r[j][1]
            if k_now >= ks[i][1]:
                print(cnt)
                break

    elif ks[i][1] < ks[i][0]:
        k_now = ks[i][0]
        for j in range(d):
            cnt += 1
            if r[j][1] >= k_now >= r[j][0]:
                k_now = r[j][0]
            if k_now <= ks[i][1]:
                print(cnt)
                break
    else:
        print(0)

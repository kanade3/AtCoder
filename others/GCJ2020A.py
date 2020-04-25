t = int(input())
ans = []
for i in range(t):
    n = int(input())
    a = []
    for j in range(n):
        a.append(list(map(int, input().split())))
    cnt_sum = 0
    for j in range(n):
        cnt_sum += a[j][j]

    cnt_w = 0
    cnt_h = 0
    for j in range(n):
        if len(a[j]) != len(set(a[j])):
            cnt_w += 1

    for j in range(n):
        h_list = [a[k][j] for k in range(n)]
        if len(h_list) != len(set(h_list)):
            cnt_h += 1

    ans.append([cnt_sum, cnt_w, cnt_h])

for i in range(t):
    print("Case #{}:".format(i+1), end=' ')
    print(*ans[i])

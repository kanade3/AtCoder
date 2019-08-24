m, d = map(int, input().split())
cnt = 0
for i in range(1, m + 1):
    for j in range(1, d + 1):
        # print(i, j)
        if j % 10 >= 2 and (j // 10) >= 2 and j % 10 * (j // 10) == i:
            cnt += 1
print(cnt)

n = int(input())

ans = []
for i in range(n):
    i_ans = []
    t = str(int(input()))

    cnt_10 = 0
    check_num = len(t) - 1
    while check_num >= 0:
        if t[check_num] != '0':
            i_ans.append(int(t[check_num]) * 10 ** cnt_10)
        cnt_10 += 1
        check_num -= 1
    ans.append(i_ans)

for i in range(n):
    print(len(ans[i]))
    print(*ans[i])

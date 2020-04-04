from collections import deque

k = int(input())
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
q = deque(['0'])
cnt = 0
ans = []
while len(q):
    v = q.pop()
    # print(v, cnt)
    if k + 1 == cnt:
        print(ans[-1])
        # print(ans)
        exit()
    check = int(v[-1])

    # print(v, check)

    for plus in n:
        st = str(v) + str(plus)

        if str(st)[0] == '0' and str(st)[1] == '0':
            continue

        if len(st) > 12:
            continue

        if abs(check - plus) > 1 and len(st) != 2:
            # print(check, plus, str(v) + str(plus))
            continue
        cnt += 1
        if k + 1 == cnt:
            ans_show = ans[-1]
            for g in range(len(ans_show)):
                if g == 0 and ans_show[0] == '0':
                    pass
                else:
                    print(ans_show[g], end='')
            exit()
        # print(q)
        ans.append(str(v) + str(plus))
        q.appendleft(st)

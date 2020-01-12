n, m = map(int, input().split())
cnt = 0
ac_cnt = 0
wa_cnt = 0
ans_flag = 0
bp = -1
d = []
for i in range(m):
    a, b = map(str, input().split())
    d.append([a, b])
d.sort(key=lambda x: x[0])
# print(d)
for i in range(m):
    p, s = d[i][0], d[i][1]
    # print(p, s)
    if bp != p:
        cnt = 0
        ans_flag = 0
    if s == 'WA' and ans_flag == 0:
        cnt += 1
    elif s == 'AC' and ans_flag == 0:
        ac_cnt += 1
        wa_cnt += cnt
        cnt = 0
        ans_flag = 1
    bp = p

print(ac_cnt, wa_cnt)

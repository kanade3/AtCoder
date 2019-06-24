n, k = map(int, input().split())
S = input()
a = []
if S[len(S) - 1] == "1":
    S += '0'
else:
    S += '1'
# print(S)
cur = 0
cntdif = 0
while cur != len(S) - 1:
    cntdif += 1
    if S[cur] != S[cur + 1]:
        a.append(cntdif)
        cntdif = 0
    cur += 1
# print(a)

countsum = 0
printmax = 0
m = 0
if k == 1:
    cnv = 2
else:
    cnv = 2 * k + 1
while 1:
    for i in range(cnv):
        if i + m > len(a) - 1:
            printmax = max(printmax, countsum)
            print(printmax)
            exit()
        countsum += a[i + m]
    printmax = max(printmax, countsum)
    countsum = 0
    m += 1

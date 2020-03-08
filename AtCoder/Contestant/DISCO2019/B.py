n = int(input())
a = list(map(int, input().split()))
cntL = 0
s = sum(a) // 2
cntR = 0
for i in range(len(a)):
    if cntL + a[i] < s:
        cntL += a[i]
    else:
        cntR = cntL
        cntL += a[i]
        break
# print(cntL)
print(min(abs((sum(a) - cntL) - cntL), abs(sum(a) - cntR) - cntR))
# print(abs(sum(a) - cntR) - cntR)

n = int(input())
a = list(map(int, input().split()))
flag = 0
flagcnt = 0
for i in a:
    if i % 2 == 0:
        flagcnt += 1
        if i % 3 == 0 or i % 5 == 0:
            flag += 1
if flag == flagcnt:
    print("APPROVED")
else:
    print("DENIED")

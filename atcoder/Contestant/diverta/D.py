N = int(input())
a = [str(input()) for i in range(N)]
cnt = 0
tBeA = 0
tBeNA = 0
tNBeA = 0
for i in range(N):
    flag = False
    if a[i][0] == "B":
        if a[i][-1] == "A":
            tBeA += 1
        else:
            tBeNA += 1
    else:
        if a[i][-1] == "A":
            tNBeA += 1

    for j in range(len(a[i])):
        # print(a[i][j])
        if a[i][j] == "B" and flag:
            cnt += 1
        flag = False

        if a[i][j] == "A":
            flag = True

print(
    cnt + min(tBeNA, tNBeA) if tBeA == 0 else cnt + min(tBeNA, tNBeA) + tBeA if tNBeA + tBeNA > 0 else cnt + min(tBeNA,
                                                                                                                 tNBeA) + tBeA - 1)

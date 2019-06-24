N = int(input())
a=[int(i) for i in input().split()]

cur = len(a)-1
hozon = 0
pr = 0
chfl = False
while (cur >= 1):
    if a[cur] != 1 and a[cur] > a[cur - 1]:
        chfl = True
        hozon = cur
        tmp = a[cur]
        a[cur] = a[cur - 1]
        a[cur] = tmp
        if cur + 1 <= len(a)-1:
            cur += 1
    elif chfl  and a[cur] <= a[cur - 1]:
        cur = hozon - 1


    elif a[cur] == 1:
        for i in range(pr):
            print(a[cur + i])

        pr = 0
    else:
        cur -= 1
        pr += 1

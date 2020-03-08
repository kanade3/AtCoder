n = int(input())
a = list(map(int, input().split()))
for i in range(len(a) - 1, -1, -1):
    if a[i] == 1:
        cntnum = 2
        num = 1
        for j in range(i + 1, len(a)):
            if a[j] == cntnum:
                num += 1
                cntnum += 1
        print(n - num)
        exit()

print(-1)

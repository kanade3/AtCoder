n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

a.sort(key=lambda x: x[1])

cnt = 0
for i in range(n):
    cnt += a[i][0]
    # print(cnt, a[i][1])
    if cnt > a[i][1]:
        print('No')
        exit()

print('Yes')

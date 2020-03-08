n = int(input())
p = list(map(int, input().split()))
cnt = 0
for i in range(n - 2):
    a = list()
    a.append(p[i])
    a.append(p[i + 1])
    a.append(p[i + 2])
    check = p[i + 1]
    a.sort()
    if check == a[1]:
        cnt += 1
print(cnt)

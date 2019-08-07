n = int(input())
cnt = 0
a = []
a.append(0)
for i in range(1, n + 1):
    a.append(str(i))
    if len(a[i]) % 2 == 1:
        cnt += 1
print(cnt)

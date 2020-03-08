a = sorted(list(map(int, input().split())))
cnt = 0
while a[1] != a[2]:
    a[0] += 1
    a[1] += 1
    cnt += 1

while a[0] < a[2]:
    a[0] += 2
    cnt += 1
if (a[2] - a[0]) % 2 == 1:
    cnt += 1
print(cnt)

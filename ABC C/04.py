n = int(input())

a = [1, 2, 3, 4, 5, 6]

rotate = (n-1) % 30
i = 0
cnt = 0
while cnt <= rotate:
    a[i], a[i + 1] = a[i + 1], a[i]
    i += 1
    cnt += 1
    if i + 1 > 5:
        i = 0
    # print(a)

for i in a:
    print(i, end='')

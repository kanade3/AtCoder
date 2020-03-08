n, m = map(int, input().split())
a = []

for i in range(m):
    p, y = map(int, input().split())
    a.append([p, y, i, 0])

a.sort(key=lambda x: x[1])
a.sort(key=lambda x: x[0])

# print(a)

count_l1 = a[0][0]
index = 0
for i in range(m):
    if i == 0:
        a[0][3] = 1
        index = 1
    else:
        if count_l1 == a[i][0]:
            index += 1
            a[i][3] = index
        else:
            index = 1
            count_l1 = a[i][0]
            a[i][3] = index
    # print(a[i])

a.sort(key=lambda x: x[2])

for i in range(m):
    print('{:06}{:06}'.format(a[i][0], a[i][3]))

a = [input().split() for i in range(4)]

for i in range(3, -1, -1):
    a[i].reverse()
    print(' '.join(a[i]))

n = int(input())
a = [int(input()) for _ in range(n)]
a.sort(reverse=True)
vmax = a[0]
for i in a:
    if i != vmax:
        print(i)
        exit()

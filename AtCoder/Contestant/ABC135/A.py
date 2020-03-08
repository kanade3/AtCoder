a = list(map(int, input().split()))
a.sort()
if (a[0] + a[1]) % 2 == 0:
    print(a[0] + (a[1] - a[0]) // 2)
else:
    print("IMPOSSIBLE")

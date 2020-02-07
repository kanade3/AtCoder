n = int(input())
a = list(map(int, input().split()))
l = max(a)
b = l / 2
r = 0
m = 10 ** 9
for i in range(n):
    if abs(a[i] - b) < m:
        m = abs(a[i] - b)
        r = a[i]

if n == 2:
    print(a[0], a[1])
else:
    print(l, r)

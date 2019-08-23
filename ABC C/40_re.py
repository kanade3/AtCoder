n = int(input())
a = list(map(int, input().split()))

d = [0] * n
d[1] = abs(a[1] - a[0])

for i in range(2, n):
    d[i] = min(d[i - 2] + abs(a[i] - a[i - 2]), d[i - 1] + abs(a[i] - a[i - 1]))
print(d[-1])

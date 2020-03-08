n = int(input())
a = list(map(int, input().split()))
out = [0] * n

x = 0
for i in range(n):
    if i % 2 == 1:
        x -= a[i]
    else:
        x += a[i]
out[0] = x / 2

for i in range(n - 1):
    out[i + 1] = a[i] - out[i]

for i in range(n):
    print(int(2 * out[i]), end=' ')

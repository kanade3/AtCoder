n = int(input())
a = list(map(int, input().split()))
c = [0]
d = c + a
v = [0] * (n+1)
for i in range(n, 1, -1):
    s = 0
    for j in range(2 * i, n + 1, i):
        if i % j == 0:
            s ^= v[j]
    d[i] = (s ^ v[i])

print(d.count(0))
for i in range(1, len(d)):
    if d[i] != 0:
        print(i, end=' ')

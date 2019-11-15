N = int(input())
c = [0]
a = list(map(int, input().split()))
b = [0 for _ in range(N + 1)]

d = c + a

for i in range(N, 0, -1):
    s = 0
    for j in range(2 * i, N + 1, i):
        s ^= b[j]

    b[i] = (s ^ d[i])

# print(b)
print(b.count(1) if b.count(1) else 0)
for i in range(1, len(b)):
    if b[i] != 0:
        print(i, end=' ')



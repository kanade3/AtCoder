n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]

h.sort()

tmp = 10 ** 10

for i in range(n):
    if i + k - 1 >= len(h):
        break
    tmp = min(tmp, h[i + k - 1] - h[i])

print(tmp)

n, y = map(int, input().split())

res = 0
for i in range(n + 1):
    for j in range(n + 1):
        k = n - i - j
        if k >= 0 and 10000 * k == y - 1000 * i - 5000 * j:
            print(k, j, i)
            exit()
print(-1, -1, -1)

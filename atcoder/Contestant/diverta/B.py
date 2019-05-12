r, g, b, n = map(int, input().split())
cnt = 0
for i in range(n + 1):
    for j in range(n + 1):
        T = i * r + j * g
        if T > n:
            break

        if (n - T) % b == 0:
            cnt += 1
print(cnt)

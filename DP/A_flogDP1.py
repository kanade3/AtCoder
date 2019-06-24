n, k = map(int, input().split())
a = [int(i) for i in input().split()]

INF = 10 ** 9
dp = [INF] * n

# 初期条件
dp[0] = 0

# min(dp[to], dp[from] + (矢印の重み));
for i in range(n):
    for j in range(1, k + 1):
        if i+j < len(a):
            dp[i + j] = min(dp[i + j], dp[i] + abs(a[i] - a[i + j]))

# print(dp)
print(dp[n - 1])

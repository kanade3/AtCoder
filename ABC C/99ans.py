N = int(input())
INF = 10 ** 8
dp = [INF] * (N + 10)
dp[0] = 0
for i in range(1, N + 1):
    p = 1
    while i >= p:
        dp[i] = min(dp[i], dp[i - p] + 1)
        p *= 6
    p = 1
    while i >= p:
        dp[i] = min(dp[i], dp[i - p] + 1)
        p *= 9
print(dp)
print(dp[N])

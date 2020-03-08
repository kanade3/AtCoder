n = int(input())
INF = 10 ** 8
dp = [INF] * 100010
dp[0] = 0

for i in range(1, n + 1):
    p = 1
    while p <= i:
        dp[i] = min(dp[i], dp[i - p] + 1)
        p *= 6

    p = 1
    while p <= i:
        dp[i] = min(dp[i], dp[i - p] + 1)
        p *= 9

print(dp[n])

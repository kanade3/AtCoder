n = int(input())
a = [int(i) for i in input().split()]

dp = [0] * n

dp[1] = abs(a[0] - a[1])

for i in range(2, n):
    dp[i] = min(dp[i - 2] + abs(a[i] - a[i - 2]), dp[i - 1] + abs(a[i] - a[i - 1]))

print(dp)
print(dp[n-1])

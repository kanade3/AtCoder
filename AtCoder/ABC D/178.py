s = int(input())

dp = [0] * 2020
dp[0] = 1
wari = 10 ** 9 + 7
for i in range(3, s + 1):
    for j in range(3, s + 1):
        dp[i] = (dp[i] + dp[i - j]) % wari

print(dp[s])

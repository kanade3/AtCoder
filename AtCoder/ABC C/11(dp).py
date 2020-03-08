n = int(input())
a = [int(input()) for _ in range(3)]
if n in a:
    print('NO')
    exit()

dp = [10 ** 9] * (n + 1)
dp[n] = 0

for i in range(n, 0, -1):
    if i in a:
        continue
    for j in range(1, 4):
        dp[i - j] = min(dp[i] + 1, dp[i - j])
print('YES' if dp[0] <= 100 else 'NO')

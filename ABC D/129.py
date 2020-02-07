import sys

input = sys.stdin.readline
n, m = map(int, input().split())


bt = [int(input()) for _ in range(m)]
br = set(bt)
dp = [0 for _ in range(n + 1)]

dp[0] = 1
if 1 not in br:
    dp[1] = 1
for i in range(2, n + 1):
    if i in br:
        continue
    else:
        dp[i] = (dp[i - 1] + dp[i - 2]) % (10**9+7)

print(dp[-1])

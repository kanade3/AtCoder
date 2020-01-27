h, n = map(int, input().split())
l = []
for i in range(n):
    a, b = map(int, input().split())
    l.append([a, b])
INF = 10 ** 9 + 11
dp = [INF] * (h + 1)
dp[0] = 0
nextj = 0
for i in range(n):
    for j in range(h):
        nextj = j + l[i][0]
        if nextj <= h:
            dp[nextj] = min(dp[nextj], dp[j] + l[i][1])
        else:
            dp[h] = min(dp[h], dp[j] + l[i][1])
print(dp[-1])
# hベースのDP式を立てる。MPベースにすると計算量が追いつかない。

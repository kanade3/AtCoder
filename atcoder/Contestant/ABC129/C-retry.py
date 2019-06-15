n, m = map(int, input().split())
a = [0 for i in range(n + 1)]

# 階段kをn+1段作り、通れない場所を1とおく
for i in range(m):
    a[int(input())] = 1

# 通れる数リスト=DPを作成→0で初期化
dp = [0] * (n + 1)

# 初期化 最初は1通りで通れるので初期化する値は1
dp[0] = 1

if a[1] == 0:
    dp[1] = 1
else:
    dp[1] = 0

for i in range(2, n + 1):
    if a[i] == 0:
        dp[i] = (dp[i - 1] + dp[i - 2]) % (10 ** 9 + 7)
    else:
        dp[i] = 0

print(dp[n])

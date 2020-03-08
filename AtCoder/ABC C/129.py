n, m = map(int, input().split())
# 辞書型,set型にすることでリストよりも圧倒的に早く回すことができる
# https://qiita.com/cof/items/05f6ffc6d4e5b062aaa9
p = {int(input()) for _ in range(m)}
s = 10 ** 9 + 7

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
if 1 in p:
    dp[1] = 0

for i in range(2, n+1):
    if i in p:
        continue
    dp[i] = (dp[i - 1] + dp[i - 2]) % s

print(dp[-1])

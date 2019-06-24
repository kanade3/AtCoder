n = int(input())
a = [int(i) for i in input().split()]
INF = 10 ** 9
dp = [INF] * n


def rec(i):
    if dp[i] < INF:
        return dp[i]

    # 足場0のコストを0にする
    if i == 0:
        return 0

    # i-1とi-2を試す
    # 一番上にresを設定。
    res = INF
    res = min(res, rec(i - 1) + abs(a[i] - a[i - 1]))

    if (i > 1):
        res = min(res, rec(i - 2) + abs(a[i] - a[i - 2]))

    # メモ化再帰。メモする
    dp[i] = res
    print(dp)
    return dp[i]


print(rec(n - 1))

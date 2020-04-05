a = list(map(int, input().split()))
n = sum(a)
x = [[0] * a[i] for i in range(3)]
vis = [False] * 10
ans = 0

# jは深さを表す。深さを1増やすごとに条件を満たしているかのチェックを行なっている
def dfs(i, j):
    global ans
    if j >= a[i]:
        i += 1
        j = 0
    if i == 3:
        ans += 1
        return
    for k in range(1, n + 1):
        print(x,i,j,k)
        if not vis[k]:
            x[i][j] = k
            if i > 0 and k < x[i - 1][j]:
                continue
            if j > 0 and k < x[i][j - 1]:
                continue
            vis[k] = True
            dfs(i, j + 1)
            vis[k] = False


dfs(0, 0)
print(ans)
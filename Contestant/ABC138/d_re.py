N, Q = map(int, input().split())

node = [[] for i in range(N + 1)]

# 木の作成。何番目が何番目と繋がっているかがわかる。
for i in range(N - 1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)
print(node)

# iばん目より下の子に加算するコストを計測する
cnt = [0 for i in range(N + 1)]
for i in range(Q):
    p, x = map(int, input().split())
    cnt[p] += x
print(cnt)


# sは今何番目を見ているか。pはその親
def dfs(s, p):
    # それぞれのnodeが繋がってる所を全部をみる
    for j in node[s]:
        # 親からきたときは親の分は加算しない。
        if j == p:
            continue
        cnt[j] += cnt[s]
        # 引数を渡すときは、次の参照すべき親は今の親であるので、今見てる番号を親として渡す必要がある。
        dfs(j, s)


dfs(1, -1)

print(*cnt)

h, w, k = map(int, input().split())

ans, z, a = [], [], []
c = 0
# 列
for i in range(h):
    # 列が変わったらとりま+1。列が全部'.'なら後から引く
    c += 1
    flag = True
    d = []
    # 列ごとに標準入力から読み取る
    tmp = input()

    if tmp == '.' * w:
        # この列では分割されないので加算した1を引いておく
        c -= 1
        ans.append([0] * w)

        # 0の列番号をリストに格納する
        z.append(i)

    else:
        # 0以外の列番号をリストに格納する
        a.append(i)
        for j in range(w):
            if tmp[j] == '#':
                # その列の最初の#なのかどうかを判断する
                # 2個目の#からcの値を増やすようにするため
                if flag:
                    flag = False

                else:
                    c += 1
            # dにはその行の数情報が追加される(列ごとに初期化される)
            d.append(c)
        # その行の結果を追加する
        ans.append(d)

for i in z:
    # 最初にない場合は後ろのいちごのある列にマージさせる操作
    if i < a[0]:
        ans[i] = ans[a[0]]
    else:
        # その他の場合は前の列にマージ
        ans[i] = ans[i - 1]
for i in range(h):
    print(ans[i])
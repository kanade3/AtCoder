from collections import *

n, m = map(int, input().split())
# defaultdictは引数に関数をとってdictを初期化する
d = defaultdict(list)

for i in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)
    # print(d)

# d[i]はiと友達の番号を表す
# 例　{1: [2], 2: [1, 3], 3: [2]})　1は2と友達、2は1と3と友達

for i in range(1, n + 1):
    ans = set()
    for j in d[i]:
        print(d[i]+[i])
        # | はor演算子 d[i]+[i]で自分の番号をリストに突っ込み、それで自分をカウントしないようにしてる。
        # d[i]番目の要素一つ一つに対して↑の要素に合致しなかったら、友達の友達ということなので論理和をとる。
        ans = ans | set([k for k in d[j] if k not in d[i] + [i]])
        print(ans)

    # print(len(ans))

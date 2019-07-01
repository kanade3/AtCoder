import math

n, k = map(int, input().split())


def combinations_count(N, R):
    return math.factorial(N) // (math.factorial(N - R) * math.factorial(R))


for i in range(1, k + 1):
    # 注意！もし青玉の置く場所がiより少なかったら置くことができないので、0通り
    if n - k + 1 < i:
        print(0)
    else:
        answer = combinations_count(k - 1, i - 1) * combinations_count(n - k + 1, i)
        # print(combinations_count(i - 1 + k, i - 1), combinations_count(n - k + 1, i))
        print(answer % (10 ** 9 + 7))

# 赤玉はn-k個。すなわち赤玉＋１の場所に置くことができる。

# 青の組みの分け方、（１、２）（２、１）等＊置く場所（n-k+1)C i ただしiは　i回操作のi

# まず、全部の組みの分け方（n=2)なら二つを分配する。（０であると分配したことにならないので）
# そして残りの個数を分配する方法(それぞれの玉についてどれに入れるか＝n-1!)を探せば良いから、(ただし、被りはのぞく。）例1,1と1,1

# たまの分配では数学の確率の仕切り棒の考え方を使うのが有効？？仕切り棒はi-1個
# i-1=仕切り棒の数　i-1+k=青球＋仕切り

# ↑仕切り棒の考え方だと、同じものの連続では重複してしまう、例（(1,2)と(2,1)）なのでK-1個のボールからi-1個選ぶという手法を用いる。

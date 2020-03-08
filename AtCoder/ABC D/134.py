n = int(input())
a = list(map(int, input().split()))
c = [0]
d = c + a
s = [0 for _ in range(n + 1)]

for i in range(n, 0, -1):
    # 今注目してるiについて、その倍数に当たる部分の球の和を合わせる。そのための変数wを定義する
    w = 0
    for j in range(2 * i, n + 1, i):
        # 2で割ったあまりなのでXORをとる
        # wは現段階での格納されている個数(あまりで表現される)
        w ^= s[j]
    # wと入力(i)を一致させ,出力用のsに格納する
    s[i] = (w ^ d[i])

print(sum(s))
for i in range(1, n + 1):
    if s[i] != 0:
        print(i, end=' ')

n, m = map(int, input().split())
# n+1段登る
a = [0 for i in range(n + 1)]

# 通れない場所を1とする
for i in range(m):
    a[int(input())] = 1

# 通れる数を記録するリストを作成。0で初期化
c = [0 for i in range(n + 1)]
# nはn-1,n-2を参照するようにする。最初は1。
c[0] = 1
# 最初が通れるか否かを判断
if a[1] == 0:
    c[1] = 1
else:
    c[1] = 0
# 1は計算したので次は2~
for i in range(2, n + 1):
    if a[i] == 0:
        c[i] = (c[i - 1] + c[i - 2]) % (10 ** 9 + 7)
    else:
        c[i] = 0
# print(c)
print(c[n])

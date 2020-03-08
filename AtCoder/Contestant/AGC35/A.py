import collections

N = int(input())
a = [int(i) for i in input().split()]
b = collections.Counter(a)
flag = False

# 条件1 全部0だったらOK
if all(i == 0 for i in a):
    flag = 1
# 条件2 2*3/Nがxが書かれていて、残りは0ならOK これは0の個数確定＋二種の数字で確定できる。
elif N % 3 == 0 and len(b) == 2 and b['0'] == N // 3:
    flag = 1
# 条件3 xとyとzのXORをとり、それが0となるような3つの相違なる整数がN/3存在
elif N % 3 == 0 and len(b) == 3:
    # 連想配列のキーとなる数（数字の種類をリスト化）
    k = list(b.keys())
    if k[0] ^ k[1] ^ k[2] == 0 and all(b.count(i) == N // 3 for i in k)
        # all(i == N / 3 for i in k)
        print(N//3)
        print(k[0])
        flag = 1

print('Yes' if flag else 'No')

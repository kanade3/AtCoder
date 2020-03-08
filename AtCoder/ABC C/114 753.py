N = int(input())


def dfs(s):
    # 入力したものが最大値nを超えていたら今までの結果を返す
    if int(s) > N:
        return 0
    # そうでなければ、まず、s自身が753数であるかを判断する(ここでoutを初期化)
    out = 1 if all(s.count(i) > 0 for i in '753') else 0

    # 判断が終了したら再帰をする
    for x in '753':
        # outのそれぞれの結界に足し合わせる
        out += dfs(s + x)
    return out


print(dfs('0'))

'''
# 順番に探して行ったらきりがないので、「空っぽのものから初めて持っているものの後ろに7,5,3を付け足してそれが条件の範囲内にあるかを調べる」


def dfs(s):  # sではじまる文字列の753数の数を数える
    if int(s) > N:
        return 0
    # sが753数なら+1
    ret = 1 if all(s.count(c) > 0 for c in '753') else 0
    for c in '753':
        # 再帰
        ret += dfs(s + c)
    return ret


print(dfs('0'))

# 問題文の3つめのケースでは、入力の値が大きいことに対して出力の値がちょい少ないのがヒントになっている。
'''

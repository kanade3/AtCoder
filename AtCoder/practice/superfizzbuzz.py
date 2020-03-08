# https://atcoder.jp/contests/nikkei2019-ex/tasks/nikkei2019ex_f

n = int(input())
for i in range(1, n + 1):
    out = ""
    if i % 2 == 0:
        out += "a"
    if i % 3 == 0:
        out += "b"
    if i % 4 == 0:
        out += "c"
    if i % 5 == 0:
        out += "d"
    if i % 6 == 0:
        out += "e"

    print(out if out else i)

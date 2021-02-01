# https://atcoder.jp/contests/arc026/tasks/arc026_1

n, a, b = map(int, input().split())

if n > 5:
    print(b * 5 + a * (n - 5))
else:
    print(b * n)

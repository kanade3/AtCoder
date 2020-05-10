# 1番目から順番に考えてみて、何番目でシフト数が上がるかを考えるとb-1が見えてくる。
n = int(input())

while n:
    a, b = map(int, input().split())
    shift = (b - 1) // (a - 1)
    print(b + shift)
    n -= 1

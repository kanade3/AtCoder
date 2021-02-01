# https://atcoder.jp/contests/arc009/tasks/arc009_1
n = int(input())
sum = 0
for i in range(n):
    a, b = map(int, input().split())
    sum += a * b
print(int(sum * 1.05))

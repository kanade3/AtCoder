# https://atcoder.jp/contests/arc002/tasks/arc002_1

y = int(input())
flag = 0

if y % 400 == 0:
    flag = True
elif y % 100 != 0 and y % 4 == 0:
    flag = True
print("YES" if flag else "NO")

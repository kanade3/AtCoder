# https://atcoder.jp/contests/soundhound2018-summer-qual/tasks/soundhound2018_summer_qual_a
a, b = map(int, input().split())
if a + b == 15:
    print('+')
elif a * b == 15:
    print('*')
else:
    print('x')

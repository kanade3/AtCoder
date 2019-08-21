import math
n = int(input())
a = map(int, input().split())
cnt = 0
s = 0
for i in a:
    if i != 0:
        cnt += 1
        s += i
print(math.ceil(s / cnt))

import math

s = input()
a = [0] * len(s)
cnt = 0
# Rを見る
for i in range(len(s)):
    if s[i] == 'R':
        cnt += 1
    else:
        a[i] += math.floor(cnt / 2)
        a[i - 1] += math.ceil(cnt / 2)
        cnt = 0

# Lを見る(逆から)

cnt = 0
for i in range(len(s)-1, -1, -1):
    if s[i] == 'L':
        cnt += 1
    else:
        a[i] += math.floor(cnt / 2)
        a[i + 1] += math.ceil(cnt / 2)
        cnt = 0

for i in a:
    print(i, end=' ')

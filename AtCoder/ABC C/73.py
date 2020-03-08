import collections

n = int(input())
a = [int(input()) for _ in range(n)]
b = collections.Counter(a)

cnt = 0
for v in b.values():
    if v % 2 == 1:
        cnt += 1

print(cnt)

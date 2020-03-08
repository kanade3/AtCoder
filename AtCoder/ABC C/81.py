import collections

n, k = map(int, input().split())
a = list(map(int, input().split()))

c = collections.Counter(a).most_common()

cnt = 0
cntdiff = 0
for i, j in c:
    cntdiff += 1
    if cntdiff > k:
        cnt += j
print(cnt)

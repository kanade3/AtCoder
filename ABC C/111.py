import collections, math

cnt = 0
n = int(input())
v = list(map(int, input().split()))

a = collections.Counter()
b = collections.Counter()
for i in range(0, n, 2):
    a[v[i]] += 1
for i in range(1, n, 2):
    b[v[i]] += 1

e = math.ceil(n // 2)
a1 = a.most_common()[0]
a2 = a.most_common()[1]
b1 = b.most_common()[0]
b2 = b.most_common()[1]
va1 = e - a1
va2 = e - a2
vb1 = n - e - b1
vb2 = n - e - b2

if max(a.keys()) == max(b.keys()):
    cnt = min(va2 + vb1, va1 + vb2)
else:
    cnt = va1 + vb1
print(cnt)

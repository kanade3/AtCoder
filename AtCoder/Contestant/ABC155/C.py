import collections

n = int(input())
a = []
for i in range(n):
    a.append(input())

c = collections.Counter(a)
d = c.most_common()
e = d[0][1]
f = []
for i, j in d:
    if e == j:
        f.append(i)
f.sort()

for i in f:
    print(i)
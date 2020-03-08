import collections

n = int(input())
d = list(map(int, input().split()))
for i in range(len(d)):
    if i == 0 and d[i] != 0:
        print(0)
        exit()
    if i != 0 and d[i] == 0:
        print(0)
        exit()

e = collections.Counter(d)

e2 = dict(sorted(e.items()))
e3 = list(e2.values())
e4 = list(e2.keys())
print(e2)
print(e3)
print(e4)

tmp = 0
for i in e4:
    if i - tmp >= 2:
        print(0)
        exit()
    tmp = i

cntsum = 1
for i in range(1, len(e3)):
    cntsum *= e3[i - 1] ** e3[i]
print(cntsum%998244353)

import collections

n = int(input())
d = list(map(int, input().split()))
e = collections.Counter(d)

if d[0] != 0:
    print(0)
    exit()

cntsum = 1
judge_cnt = 0

if e[1] == 0:
    print(0)
    exit()

m = max(e)
e2 = dict(sorted(e.items()))
print(e2)
beforekey = 1
for i in e2.keys():
    if i != 0:
        cntsum = cntsum * e2[beforekey] ** e2[i]

    if i - beforekey > 1:
        print(0)
        exit()
    beforekey = i

print(cntsum)

import collections

n = int(input())
a = list(map(int, input().split()))

b = collections.Counter(a)
c = b.most_common()
c.sort(key=lambda x: x[0])
cnt = 1
if n % 2 == 1:
    cnt = 0

for i, j in c:
    # print(i, j)
    if cnt == 0:
        if j != 1:
            print(0)
            exit()
        else:
            cnt += 2
    else:
        if i != cnt or j != 2:
            print(0)
            exit()
        else:
            cnt += 2

print((2 ** (n // 2)) % (10 ** 9 + 7))

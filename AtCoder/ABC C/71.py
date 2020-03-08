import collections

n = int(input())
a = collections.Counter(list(map(int, input().split())))
s = []
for k, v in sorted(a.items(), key=lambda x: -x[0]):
    # print(k,v)

    if v > 1:
        s.append(k)
        if len(s) > 1:
            print(s[0] * s[1])
            exit()

    if v >= 4:
        print(k ** 2)
        exit()
print(0)

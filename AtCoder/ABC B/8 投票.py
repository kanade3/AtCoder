import collections

n = int(input())
a = [input() for _ in range(n)]

b = collections.Counter(a)
print(b.most_common()[0][0])

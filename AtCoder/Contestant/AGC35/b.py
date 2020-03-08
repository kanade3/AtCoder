import collections

a = [2, 3, 4, 4, 3, 2, 4, 5, 1]
b = collections.Counter(a)
c = list(b.keys())
print(c)
print(c[0] ^ c[1])

import collections

n = int(input())
a = list(map(int, input().split()))

for i in range(len(a)):
    a.append(int(a[i] - 1))
    a.append(int(a[i] + 1))

b = collections.Counter(a)
print(b.most_common()[0][1])
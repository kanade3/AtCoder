import collections

n = int(input())
a = list(map(int, input().split()))
b = collections.Counter(a)
for i in range(n):
    print(b[i+1])

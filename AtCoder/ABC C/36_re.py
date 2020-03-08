import sys

input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
b = sorted(set(a))

m = {}
for i, j in enumerate(b):
    m.update({j: i})

for i in a:
    print(m[i])

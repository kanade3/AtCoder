import sys

input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]

d = {i: v for v, i in enumerate(sorted(set(a)))}

for i in a:
    print(d[i])

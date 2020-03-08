import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]

b = list(set(a))

for i in range(n):
    print(b.index(a[i]))

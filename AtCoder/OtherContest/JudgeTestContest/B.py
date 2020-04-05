from collections import deque

n = int(input())
r = []
b = []
for i in range(n):
    N, C = map(str, input().split())
    if C == 'B':
        b.append(int(N))
    else:
        r.append(int(N))

R = deque(sorted(r,reverse=True))
B = deque(sorted(b,reverse=True))
for i in range(n):
    if len(R) > 0:
        print(R.pop())
    else:
        print(B.pop())

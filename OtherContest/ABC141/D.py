# wrong code
import bisect
import math
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
for i in range(m):
    # print(a)
    # print(math.floor(a[-1] / 2))
    b = bisect.bisect_left(a, math.floor(a[-1] / 2))
    a.insert(b, math.floor(a[-1] / 2))
    a.pop(-1)

    if len(a) == 1:
        print(math.floor(a[0] / 2**(m - i - 1)))
        exit()
print(sum(a))


##
N, M= map(int, input().split())
A = list(map(int,input().split()))
A=[-1*a for a in A]
import heapq
import math
hq=heapq.heapify(A)
for m in range(M):
    X=heapq.heappop(A)
    heapq.heappush(A,math.ceil(X/2))
print(sum(A)*-1)

import heapq

n, m = map(int, input().split(" "))

a = [- int(i) for i in input().split(" ")]
heapq.heapify(a)

for _ in range(m):
    largest = heapq.heappop(a)
    heapq.heappush(a, int(largest / 2))

print(- sum(a))
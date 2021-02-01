# https://atcoder.jp/contests/abc166/tasks/abc166_e
from collections import Counter

n = int(input())
a = list(map(int, input().split()))

left = []
right = []

for i in range(n):
    left.append(a[i] + (i + 1))
    right.append((i + 1) - a[i])
# print(left, right)

C = Counter(right)
# print(C)

ans = 0
for I in left:
    ans += C[I]
    # print(I,ans)
print(ans)

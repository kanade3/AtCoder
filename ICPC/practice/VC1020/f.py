from collections import Counter

n = int(input())
a = list(map(int, input().split()))

b = [[] for i in range(n)]

for i in range(n * 2):
    b[a[i] - 1].append(i)

# print(b)

C = Counter()

for i in range(n):
    s = abs(b[i][1] - b[i][0]) - 1
    C[s] += 1
# print(C)

ans = 0
for i in range(2 * n-1):
    ans += C[i]
    print(ans)

n, k = map(int, input().split())
p = list(map(int, input().split()))
R = [0] * n
R[0] = p[0]
for i in range(1, n):
    R[i] = R[i - 1] + p[i]

tmp = 0
m = 0
index = 0
for i in range(n - k + 1):
    if m < R[i + k - 1] - tmp:
        m = R[i + k - 1] - tmp
        index = i
    tmp = R[i]
ans = 0

for i in range(index, index + k):
    ans += (p[i] + 1) / 2
print(ans)

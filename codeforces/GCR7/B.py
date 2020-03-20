n = int(input())
a = list(map(int, input().split()))
m = 0
for i in range(n):
    a[i] += m
    m = max(m, a[i])
print(*a)

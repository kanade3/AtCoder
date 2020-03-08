n, t = map(int, input().split())
a = list(map(int, input().split()))

time = 0

for i in range(n - 1):
    time += min(t, a[i + 1] - a[i])

print(time + t)

# 上はベターな解法
'''
for i in range(n-1):
    if a[i + 1] - a[i] < t:
        time += a[i + 1] - a[i]
    elif a[i + 1] - a[i] >= t:
        time += t
print(time + t)

'''

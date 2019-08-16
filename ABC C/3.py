n, k = map(int, input().split())
r = list(map(int, input().split()))
r.sort()
rate = 0
for i in range(n - k, n):
    rate = (rate + r[i]) / 2
print(rate)

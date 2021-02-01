n = int(input())
a = sorted(list(map(int, input().split())))

now = 0
ans = 0
for i in range(n):
    ans += a[i] * i - now
    now += a[i]
print(ans)

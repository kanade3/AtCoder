import fractions as math

n, x = map(int, input().split())
a = list(map(int, input().split()))
a.append(x)
a.sort()
# print(a)
gcd = a[1] - a[0]
for i in range(2, n+1):
    d = a[i] - a[i - 1]
    gcd = math.gcd(gcd, d)
print(gcd)

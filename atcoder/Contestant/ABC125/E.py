n = int(input())
*a, = map(int, input().split())


def gcd(x, y):
    return gcd(y, x % y) if y else x


l, r = [], []

for i in range(n):
    l.append(gcd(l[i - 1], a[i - 1]) if i else 0)
    r.append(gcd(r[i - 1], a[n - i]) if i else 0)
print(max([gcd(l[i], r[n - i - 1]) for i in range(n)]))

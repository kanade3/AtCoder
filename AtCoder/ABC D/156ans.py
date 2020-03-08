def choose(n, r, mod):
    x = 1
    y = 1
    for i in range(min(r, n - r)):
        x = x * (n - i) % mod
        y = y * (i + 1) % mod
    y = pow(y, mod - 2, mod)
    return (x * y) % mod


n, a, b = map(int, input().split())
mod = 10 ** 9 + 7
ans = pow(2, n, mod)
ans -= 1
ans -= choose(n, a, mod)
ans -= choose(n, b, mod)

while ans < 0:
    ans += mod
print(ans)

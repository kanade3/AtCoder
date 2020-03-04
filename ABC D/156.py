n, a, b = map(int, input().split())
mod = 10 ** 9 + 7


def choose(n, r, mod):
    r = min(r, n - r)
    x = 1
    y = 1
    for i in range(r):
        x = x * (n - i) % mod
        y = y * (i + 1) % mod
    # Python3.4.3ではpowの引数に負の数はつかえない。
    # そもそも逆元を間違って覚えてた。正しい式は K^-1 ≡ K^(M-2) (mod M)
    y = pow(y, mod - 2, mod)
    return x * y % mod


ans = pow(2, n, mod) - 1 - choose(n, a, mod) - choose(n, b, mod)

while ans < 0:
    ans += mod
print(ans)

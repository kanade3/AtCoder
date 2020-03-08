def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
# x%yすることでswapしなくても逆転する


def prime_factorize(n):
    p = []
    while n % 2 == 0:
        if 2 not in p:
            p.append(2)
        n //= 2
    # 偶数はこれからは試さなくてよくなる
    f = 3
    while f * f <= n:
        if n % f == 0:
            if f not in p:
                p.append(f)
            n //= f
        else:
            f += 2
    if n != 1 and n not in p:
        p.append(n)
    return p


a, b = map(int, input().split())
q = prime_factorize(gcd(a, b))
# print(q)
print(len(q) + 1)

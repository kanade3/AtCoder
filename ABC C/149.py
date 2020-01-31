x = int(input())


def prime_factorize(n):
    p = []
    while n % 2 == 0:
        if 2 not in p:
            p.append(2)
        n //= 2
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


if x == 1:
    print(1)
else:
    while (1):
        a = prime_factorize(x)
        if len(a) == 1 and a[0] == x:
            print(x)
            exit()
        x += 1

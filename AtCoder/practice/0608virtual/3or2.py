n = int(input())
a = list(map(int, input().split()))


def prime_factorize_n2(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a.count(2)


cnt = 0
for i in a:
    if i % 2 == 0:
        cnt += prime_factorize_n2(i)
print(cnt)

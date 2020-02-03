import collections

n = int(input())


def prime_factorize_n(n):
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
    return a


k = []
for i in range(1, n + 1):
    k = k + prime_factorize_n(i)
c = collections.Counter(k)
d = c.most_common()
ans = 1

for k, v in d:
    ans = (ans*(v + 1)) % (10 ** 9 + 7)
print(ans)

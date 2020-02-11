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


l = prime_factorize_n(n)
print(l)
A, B = 1, 1
for i in range(len(l) - 1, -1, -1):
    if A < B:
        A *= l[i]
    else:
        B *= l[i]
print(A,B)
print(max(len(str(A)), len(str(B))))

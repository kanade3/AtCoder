import fractions

n = int(input())
t = [int(input()) for _ in range(n)]

for i in range(1, n):
    t[i] = t[i] * t[i - 1] // fractions.gcd(t[i], t[i - 1])
print(t[-1])

import fractions
a, b = map(int, input().split())
print(int(a * b / fractions.gcd(a, b)))

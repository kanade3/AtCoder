n = int(input())
a, b = 0, 0
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0 and n % n // i == 0:
        a = n // i
        b = n // a
print(a + b - 2)

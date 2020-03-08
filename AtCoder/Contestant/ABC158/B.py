n, a, b = map(int, input().split())

s = n // (a + b)
amari = n - s * (a + b)

amarib = min(amari, a)
print(s * a + amarib)

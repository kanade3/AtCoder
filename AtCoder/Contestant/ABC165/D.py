a, b, n = map(int, input().split())
m = b - 1
if m > n:
    m = n
print(int((a * m - a * m % b) / b - a * ((m - m % b) / b)))

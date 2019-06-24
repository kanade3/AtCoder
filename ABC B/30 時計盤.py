n, m = map(int, input().split())
if n >= 12:
    n -= 12
print(n*0.5-m*6)

a, b, k = map(int, input().split())
a -= k
if a < 0:
    b += a
print(max(0, a), max(0, b))

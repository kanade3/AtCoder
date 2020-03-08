import math

a, b, x = map(int, input().split())
if x / a >= a * b / 2:
    h = 2 * (b - x / a ** 2)
    r = math.atan2(h, a)
else:
    w = 2 * (x / (a * b))
    r = math.atan2(b, w)

print(180 * r / math.pi)


import math

a, b, x = map(int, input().split())
s = x / a
if s >= a * b / 2:
    h = (a * b - s) * 2 / a
    r = math.atan2(h, a)

else:
    w = 2 * s / b
    r = math.atan2(b, w)
d = r * 180 / math.pi
print(d)
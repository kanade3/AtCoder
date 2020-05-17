import math

a, b, h, m = map(int, input().split())
tansin = h * 30 + m * 0.5
# tansin = min(tansin, 360 - tansin)
tyousin = m * 6

if tansin > 360:
    tansin = tansin - 360
if tyousin > 360:
    tyousin = tyousin - 360
# print(tansin)
# print(abs(tansin - tyousin))
rad = math.radians(abs(tansin - tyousin))
c = a ** 2 + b ** 2 - 2 * a * b * math.cos(rad)
print(math.sqrt(c))

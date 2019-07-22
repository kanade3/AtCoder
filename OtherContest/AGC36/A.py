import math

le = 10 ** 9
s = int(input())

y2 = math.ceil(s / le)
y1 = le * y2 - s

print(0, 0, 1000000000, y1, 1, y2)

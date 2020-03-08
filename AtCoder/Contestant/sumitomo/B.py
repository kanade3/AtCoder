import math
n = int(input())
a = math.ceil(n / 1.08)
print(a if math.floor(a * 1.08) == n else ":(")

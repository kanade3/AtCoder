import math
n = int(input())
b = int(math.log2(n)) + 1
print(2 ** b - 1)

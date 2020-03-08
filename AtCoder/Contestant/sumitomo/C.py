import math
x = int(input())
num = x // 100
amari = x % 100
# print(num,amari)
print(1 if math.ceil(amari/5) <= num else 0)

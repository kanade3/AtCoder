import math

x = int(input())
n = 100
for i in range(1, 100000):
    n = int(n * 1.01)
    if n >= x:
        print(i)
        exit()

import math

n = int(input())
a = int(math.sqrt(n))

for i in range(a + 1, 0, -1):
    if n % i == 0:
        # print(n // i, i)
        print(max(len(str(i)), len(str(n // i))))
        exit()

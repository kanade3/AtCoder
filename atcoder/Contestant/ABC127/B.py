r, d, x = map(int, input().split())
temp = x
for i in range(10):
    temp = r * temp - d
    print(temp)

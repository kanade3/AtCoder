l, r = map(int, input().split())
a = []

data = 2019

if r - l + 1 >= 2019:
    print(0)
    exit()

else:
    for i in range(l, r + 1):
        for j in range(i+1, r + 1):
            data = min(data, i * j % 2019)

print(data)

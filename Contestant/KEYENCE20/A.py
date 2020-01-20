h = int(input())
w = int(input())
n = int(input())

for i in range(1, 100000):
    if h * i >= n or w * i >= n:
        print(i)
        exit()

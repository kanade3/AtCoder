x, y = map(int, input().split())
c = 0
while 1:
    if y < x * 2 ** c:
        print(c)
        exit()
    c += 1

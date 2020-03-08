x = int(input())
i = 1
while 1:
    if (i * (i + 1)) / 2 >= x:
        print(i)
        exit()
    i += 1

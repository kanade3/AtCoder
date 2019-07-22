n = int(input())
e = 2025 - n
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == e:
            print(i, ' x ', j)

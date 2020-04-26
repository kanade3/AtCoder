a, b, c, d = map(int, input().split())

for i in range(10 ** 5):
    c -= b
    if c <= 0:
        print('Yes')
        exit()
    a -= d
    if a <= 0:
        print('No')
        exit()

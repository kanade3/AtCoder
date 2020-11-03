import random

tx = random.randint(1, 100)

with open('./test' + str(tx) + '.txt', mode='w') as f:
    for _ in range(tx):
        n = random.randint(1, 100)
        m = random.randint(1, 100)
        f.write(str(n))
        f.write(' ')
        f.write(str(m))
        f.write('\n')

        for i in range(n):
            a = random.randint(1, 10 ** 9)
            f.write(str(a))
            f.write(' ')
        f.write('\n')

        for i in range(m):
            w = random.randint(1, 10 ** 8)
            f.write(str(w))
            f.write(' ')
        f.write('\n')
    f.write('\n')
    f.write('0 0')
    f.write('\n')

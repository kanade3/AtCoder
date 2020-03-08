n = int(input())
a = [int(input()) for _ in range(3)]
if n in a:
    print('NO')
    exit()

cnt = 0
while n > 0:
    n -= 3
    if n in a:
        n += 3
        n -= 2

        if n in a:
            n += 2
            n -= 1

            if n in a:
                print('NO')
                exit()
    cnt += 1
print('YES' if cnt <= 100 else 'NO')

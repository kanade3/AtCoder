n = int(input())


def d(s):
    if len(s) == n:
        print(s)
        return 0

    for x in 'abc':
        d(s + x)


d('')
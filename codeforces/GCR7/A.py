n = int(input())


def solve(N):
    if N == 1:
        return -1
    else:
        s = ''
        s += '2'
        for j in range(N - 1):
            s += '3'
    return s


for _ in range(n):
    a = int(input())
    print(solve(a))

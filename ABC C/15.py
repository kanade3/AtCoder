n, k = map(int, input().split())
t = []
for i in range(n):
    t.append(list(map(int, input().split())))


def d(depth, xor):
    if depth == n:
        if xor == 0:
            print('Found')
            exit()
    else:
        for j in range(k):
            d(depth + 1, xor ^ t[depth][j])


d(0, 0)
print('Nothing')

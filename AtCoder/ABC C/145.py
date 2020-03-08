x, y = map(int, input().split())

mod = 10 ** 9 + 7


def choose(n, r):
    cx = 1
    cy = 1
    for i in range(r):
        cx = cx * (n - i) % mod
        cy = cy * (i + 1) % mod
    cy = pow(cy, mod - 2, mod)
    return cx * cy % mod


if (x + y) % 3 != 0:
    print(0)
    exit()
else:
    n = (x + y) // 3
    x -= n
    y -= n
    if x < 0 or y < 0:
        print(0)
        exit()
    print(choose(x + y, x))

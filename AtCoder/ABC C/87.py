n = int(input())

a = []
for i in range(2):
    a.append(list(map(int, input().split())))

b = []


def solve(i, j, k):
    if i >= 2 or j >= n:
        b.append(k)

    else:
        k += a[i][j]
        solve(i + 1, j, k)
        solve(i, j + 1, k)


solve(0, 0, 0)
print(max(b))

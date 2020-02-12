n, m, a, b = map(int, input().split())
M = []
for i in range(m):
    M.append((int(input())))

if n <= a:
    n += b

for i in range(m):
    n -= M[i]
    # print(n,M[i])
    if n < 0:
        print(i + 1)
        exit()

    if n <= a:
        n += b

print('complete')

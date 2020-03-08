N = int(input())
b = []
for i in range(N):
    b.append(input())

for i in range(N):
    for j in range(N):
        print(b[N - 1 - j][i], end='')
    print()

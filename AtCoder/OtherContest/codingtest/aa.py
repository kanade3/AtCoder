a, b = list(map(int, input().split()))
c = []
for i in range(a):
    c.append(list(map(int, input().split())))
print(c[0])

for i in range(2):
    for j in range(2):
        print(c[i][j],end=' ')
    print()

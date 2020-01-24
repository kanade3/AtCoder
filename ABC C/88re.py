s = []
a = [0, 0, 0]
b = [0, 0, 0]
for i in range(3):
    s.append(list(map(int, input().split())))

b[0] = s[0][0]
b[1] = s[0][1]
b[2] = s[0][2]

a[1] = s[1][0] - b[0]
a[2] = s[2][0] - b[0]

for i in range(1, 3):
    for j in range(1, 3):
        if s[i][j] != a[i] + b[j]:
            print("No")
            exit()
print("Yes")

n = int(input())
m, a, r, c, h = 0, 0, 0, 0, 0
for i in range(n):
    name = input()
    if name[0] == 'M':
        m += 1
    elif name[0] == 'A':
        a += 1
    elif name[0] == 'R':
        r += 1
    elif name[0] == 'C':
        c += 1
    elif name[0] == 'H':
        h += 1

s = [m, a, r, c, h]
x = [0, 0, 0, 0, 0, 0, 1, 1, 1, 2]
y = [1, 1, 1, 2, 2, 3, 2, 2, 3, 3]
z = [2, 3, 4, 3, 4, 4, 3, 4, 4, 4]

cnt = 0
for i in range(10):
    cnt += (s[x[i]] * s[y[i]] * s[z[i]])
print(cnt)
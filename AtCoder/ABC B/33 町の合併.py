N = int(input())
a = []
b = []
su = 0
for i in range(N):
    x, y = input().split()
    su += int(y)
    a.append(x)
    b.append(int(y))
for i in range(N):
    if su// 2 < b[i]:
        print(a[i])
        exit()
print('atcoder')

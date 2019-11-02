# マイナス評価のクソ解答
n, m, b = map(int, input().split())
gy, gx = map(int, input().split())

for i in range(m):
    a, b, c = map(str, input().split())

a = ['U', 'R', 'D']
print(300)
for i in range(300):
    by, bx = map(int, input().split())

    print(by, bx + 1, a[i % 3])

import math

txa, tya, txb, tyb, T, V = map(int, input().split())
n = int(input())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    before = math.sqrt((a[i][0] - txa) ** 2 + (a[i][1] - tya) ** 2)
    after = math.sqrt((a[i][0] - txb) ** 2 + (a[i][1] - tyb) ** 2)
    if before + after <= T * V:
        print('YES')
        exit()
print('NO')

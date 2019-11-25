x, y = map(int, input().split())

a = [300000, 200000, 100000]

cnt = 0
if 1 <= x <= 3:
    cnt += a[x - 1]
if 1 <= y <= 3:
    cnt += a[y - 1]
if x == 1 and y == 1:
    cnt += 400000
print(cnt)

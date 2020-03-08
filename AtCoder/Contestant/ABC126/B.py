a, b = map(int, input().split())

cnt = 0
for i in range(2):
    if a > b:
        cnt += a
        a -= 1
    else:
        cnt += b
        b -= 1
print(cnt)

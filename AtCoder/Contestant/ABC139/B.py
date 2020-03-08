cnt = 1
a, b = map(int, input().split())
tmp = a

if b == 1:
    print(0)
    exit()
while tmp < b:
    cnt += 1
    tmp += a - 1

print(cnt)

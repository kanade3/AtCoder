n, x = map(int, input().split())
a = [int(i) for i in input().split()]
cnt = 1
now = 0
for i in a:
    now += i
    if now <= x:
        cnt += 1
print(cnt)

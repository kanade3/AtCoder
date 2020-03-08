n, p = map(int, input().split())
a = list(map(int, input().split()))
a.append(100000)

cnt = 0
wa = 0
for i in range(n):
    wa += a[i]
    if wa > p:
        break
    cnt += 1

print(cnt)

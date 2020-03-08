L, R = map(int, input().split())
l = list(map(int, input().split()))
r = list(map(int, input().split()))
cnt = 0
for i in l:
    if i in r:
        r[r.index(i)] = -1
        cnt += 1
print(cnt)

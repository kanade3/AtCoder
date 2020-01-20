n = int(input())
p = list(map(int, input().split()))
c = 5*10**5
cnt = 0
for i in range(n):
    if p[i] <= c:
        cnt += 1
        c = p[i]

print(cnt)

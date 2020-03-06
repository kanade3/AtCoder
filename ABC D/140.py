n, k = map(int, input().split())
s = input()

see = s[0]
cnt = 0
cluster = 1
for i in range(1, n):
    if see == s[i]:
        cnt += 1
    else:
        see = s[i]
        cluster += 1

for i in range(k):
    if cluster > 2:
        cluster -= 1
        cnt += 2
    else:
        print(n - 1)
        exit()
print(min(cnt, n - 1))

n, l = map(int, input().split())
cnt = 10000
a = []
m = 0
for i in range(n):
    a.append(i + l)
    if cnt > abs(i + l):
        cnt = abs(i + l)
        m = i + l
print(sum(a) - m)

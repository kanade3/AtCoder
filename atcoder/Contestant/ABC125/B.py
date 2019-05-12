N = int(input())
v = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
cnt = 0
for i in range(len(v)):
    if v[i] - c[i] >= 0:
        cnt += v[i] - c[i]
print(cnt)

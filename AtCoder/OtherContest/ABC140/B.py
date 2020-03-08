n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

cnt = 0
before = -100
for i in range(n):
    cnt += b[a[i] - 1]

    if before + 1 == a[i]:
        cnt += c[before - 1]

    before = a[i]
print(cnt)

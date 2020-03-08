n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [0]
c = 0
for i in range(len(a)):
    c += a[i]
    b.append(c)

cnt = 0
i = 0
while i < len(b):
    if i >= k:
        # print(b[i], b[i - k])
        cnt += b[i] - b[i - k]
    i += 1
print(cnt)

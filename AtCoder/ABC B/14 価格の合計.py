n, x = map(int, input().split())
a = list(map(int, input().split()))
b = bin(x)

cntsum, cnt = 0, 0
for i in reversed(b):
    if i == b:
        break

    if i == "1":
        cntsum += a[cnt]
    cnt += 1

print(cntsum)

# いい解答
c = 0
for i in range(n):
  if x >> i & 1:
    c += a[i]
print(c)
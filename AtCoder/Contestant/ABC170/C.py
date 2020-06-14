x, n = map(int, input().split())
p = list(map(int, input().split()))

ans = 10 ** 9
num = 10 ** 9
a = [0] * 200
for i in range(len(p)):
    a[p[i]] = 1

for i in range(110):
    if a[i] == 1:
        continue

    if ans > abs(i - x):
        num = i
        ans = abs(i - x)

# print(num)
if abs(x - (-1)) <= abs(num-x):
    num = -1
print(num)

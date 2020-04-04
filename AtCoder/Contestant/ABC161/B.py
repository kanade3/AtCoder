n, m = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)

ng = 0
for i in range(m):
    if a[i] < sum(a) * (1 / (4 * m)):
        ng = 1
print("Yes" if not ng else "No")

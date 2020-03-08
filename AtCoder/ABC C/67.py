n = int(input())
a = list(map(int, input().split()))
sub = sum(a) - 2 * a[0]
asub = abs(sub)

for i in range(1, n - 1):
    sub -= 2 * a[i]
    if abs(sub) < asub:
        asub = abs(sub)
print(asub)

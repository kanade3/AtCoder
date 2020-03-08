n = int(input())
a = [0]
a.extend(list(map(int, input().split())))
a.append(0)
b = []
for i in range(1,n + 2):
    b.append(abs(a[i] - a[i - 1]))

s = sum(b)
for i in range(1, n+1):
    print(s - (b[i] + b[i - 1]) + abs(a[i + 1] - a[i - 1]))

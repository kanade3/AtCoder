n = int(input())
a = list(map(int, input().split()))

b = 0
for i in range(n):
    b = b ^ a[i]

for i in range(n):
    print(b ^ a[i], end=' ')

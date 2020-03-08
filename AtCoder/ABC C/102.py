n = int(input())
a = list(map(int, input().split()))
a = [a[i] - (i + 1) for i in range(len(a))]
a.sort()

median = a[len(a) // 2]
cnt = 0
for i in range(len(a)):
    cnt += abs(a[i] - median)

print(cnt)

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

cnt = 0
for i in b:
    # print(a)
    for j in range(n):
        if a[j] <= i and i - t <= a[j] <= i + t:
            # print(a[j] + t)
            cnt += 1
            a[j] = 10 ** 9
            break
print("yes" if cnt == m else "no")

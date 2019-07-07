import math

n, d = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
cnt = 0

for i in range(n):
    for j in range(n):

        if i != j:
            countwa = 0
            for k in range(d):
                countwa += abs(a[i][k] - a[j][k]) ** 2
            if float(math.sqrt(countwa)).is_integer():
                cnt += 1
print(cnt//2)
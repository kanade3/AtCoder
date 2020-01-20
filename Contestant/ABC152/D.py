n = int(input())
k = [[0] * 10 for _ in range(10)]
for i in range(n + 1):
    l = int(str(i)[0])
    r = int(str(i)[-1])
    k[l][r] += 1
ans = 0

for i in range(1, 10):
    for j in range(1, 10):
        ans += k[i][j] * k[j][i]
print(ans)

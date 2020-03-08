n = int(input())
x = sorted(list(map(int, input().split())))
# print(x)
# ans = 10 * 18 + 13
ans=[10**9]*101
for i in range(100 + 1):
    cnt = 0
    for j in range(len(x)):
        # print(x[j], i)
        # print(cnt)
        cnt = cnt + (x[j] - i) ** 2
    # ans = min(ans, cnt)
    ans.append(cnt)
print(min(ans))

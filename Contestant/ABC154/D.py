n, k = map(int, input().split())
p = list(map(int, input().split()))

ansl = 0
ansr = k-1
ans = 0
tmp = sum(p[:k])
# print(tmp)
for i in range(1,n - k+1):
    tmp = tmp - p[i-1] + p[i + k-1]
    # print(i,i+k-1,tmp)
    if tmp > ans:
        ansl = i
        ansr = i + k - 1
        ans = tmp
# print(ansl, ansr)
ans2 = 0
for i in range(ansl, ansr + 1):
    ans2 += (p[i] + 1) / 2
print(ans2)

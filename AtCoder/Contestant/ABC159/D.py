import collections

n = int(input())
a = list(map(int, input().split()))

C = collections.Counter(a)

ans = [0] * (10 ** 6)
cnt = 0
# print(C)
for i, j in C.items():
    cnt += j * (j - 1) // 2

# print(ans)
# print(cnt)
for i in range(len(a)):
    if C[a[i]] > 0:
        print(cnt - (C[a[i]]-1))
    else:
        print(cnt)

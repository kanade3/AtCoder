# https://atcoder.jp/contests/abc127/tasks/abc127_d

from collections import Counter

n, m = map(int, input().split())
a = list(map(int, input().split()))
C = Counter(a)
for i in range(m):
    b, c = map(int, input().split())
    C[c] += b

cnt = 0
ans = 0
for k, v in sorted(C.items(), reverse=True):
    # print(k, v)
    ans += k * v
    cnt += v

    if cnt > n:
        ans -= k * (cnt - n)
        print(ans)
        exit()

from collections import Counter

n = int(input())
d = list(map(int, input().split()))
d_c = Counter(d)
m = int(input())
t = sorted(list(map(int, input().split())), reverse=True)

for i in range(m):
    if d_c[t[i]] > 0:
        d_c[t[i]] -= 1
    else:
        print('NO')
        exit()
print('YES')

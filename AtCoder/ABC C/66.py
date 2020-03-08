import collections

n = int(input())
a = list(map(int, input().split()))

b = collections.deque()
for i in range(n):
    # 添字は0からなので偶奇を合わせるにはnを1引かなければならない
    if i % 2 == (n-1) % 2:
        b.appendleft(a[i])
    else:
        b.append(a[i])

for i in b:
    print(i, end=' ')

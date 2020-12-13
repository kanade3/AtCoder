import math

n, m = map(int, input().split())
if m == 0:
    print(1)
    exit()

if n == m:
    print(0)
    exit()

a = list(map(int, input().split()))
a.append(0)
a.append(n + 1)
cnt = n
cnt_list = []
s_a = sorted(a)
# print(s_a)
for i in range(1, len(s_a)):
    if s_a[i] - s_a[i - 1] <= 1:
        continue
    cnt = min(cnt, s_a[i] - s_a[i - 1] - 1)
    cnt_list.append(s_a[i] - s_a[i - 1] - 1)

wari = cnt
# print(cnt_list)
# print(cnt)

# print('------')
ans = 0
for i in range(1, len(s_a)):
    ans += math.ceil((s_a[i] - s_a[i - 1] - 1) / wari)
    # print(ans)
# print('------')
print(ans)

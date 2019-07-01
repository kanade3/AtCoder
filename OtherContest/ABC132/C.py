n = int(input())
d = list(map(int, input().split()))

d.sort()
# print(d)
this = 0
# 奇数
if n % 2 == 1:
    this = n % 2 + 1
    answer = d[this + 1] - d[this]
# 偶数
else:
    this = n // 2
    answer = d[this] - d[this - 1]

print(answer)

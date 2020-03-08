n = int(input())
a = list(map(int, input().split()))

colorlist = [0] * 8
freecolor = 0
colormin = 0
for i in a:
    if i >= 3200:
        freecolor += 1
    else:
        colorlist[i // 400] += 1


# print(colorlist)

for i in colorlist:
    if i != 0:
        colormin += 1

# 最小値
if colormin == 0:
    print(1, end=' ')
else:
    print(colormin, end=' ')

# 最大値
s = colormin + freecolor
if s > n:
    s = n
print(s)

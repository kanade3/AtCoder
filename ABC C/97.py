s = input()
k = int(input())
a = []
for i in range(len(s)):
    # rangeをlen(s)+1 からiを引くと少し計算量を減らすことができる。
    for j in range(len(s)+1):
        if j <= k:
            a.append(s[i:i + j])
# print(a)
c = sorted(set(a))
# print(c)
print(c[k])
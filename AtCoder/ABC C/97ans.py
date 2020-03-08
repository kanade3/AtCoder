s = input()
k = int(input())
substrings = []
for i in range(len(s)):
    for j in range(len(s)-i+1):
        # iにindexを合わせ、そこから何文字までを切り出すかをjで判断する。0から始まるので[]ができることに注意する。
        print('i={}, i+j={}, s[i:i+j]={}'.format(i, i+j, s[i:i+j]))
        if j <= k and s[i:i+j] != '':
            substrings.append(s[i:i+j])
substrings = sorted(set(substrings))
print(substrings)
print(substrings[k-1])
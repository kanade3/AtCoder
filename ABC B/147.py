s = input()
b = 0
l = len(s)-1
cnt = 0
while b < l:
    if s[b] != s[l]:
        cnt += 1
    b += 1
    l -= 1
print(cnt)

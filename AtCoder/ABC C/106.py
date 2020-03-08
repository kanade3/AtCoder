s = input()
k = int(input())
res = 1
index = 0
for i in range(len(s)):
    if s[i] != '1':
        res = s[i]
        index = i
        break
print(res if k > index else 1)

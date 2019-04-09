s = input()
N = int(input())
li = set()
l = [0] * 26
for i in range(len(s)):
    if i+N>len(s):
        break
    else:
        temp = s[i:i + N]
        li.add(temp)
# print(li)
print(len(li) if N <= len(s) else "0")

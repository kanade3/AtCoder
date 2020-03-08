N=int(input())
s=input()

a=0
b=0
for i in range(len(s)):
    if s[i]=='R':
        a+=1
    else:
        b+=1

print('Yes'if a>b else 'No')
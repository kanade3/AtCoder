s,l,r=map(int,input().split())
if s<l:
    s=l
elif r<s:
    s=r
print(s)
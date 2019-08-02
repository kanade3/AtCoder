import math

n = int(input())
b = math.floor(math.sqrt(n))
i = b
j = b
st = n - i * j + abs(i - j)

while (1):
    while i * (j + 1) <= n:
        j += 1
        st = min(st, (n - i * j) + abs(i - j))

    i -= 1
    if i == 0:
        print(st)
        exit(0)

# よりベターな解法
"""
n=int(input())
ans=10**5
for a in range(1,int(n**0.5)+1):
  b=n//a
  m=n-(a*b)
  ans=min(ans,abs(a-b)+m)
  
print(int(ans))
"""

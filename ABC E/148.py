n = int(input())
if n % 2 == 1:
    print(0)
    exit()
c = 10
ans = 0
while c <= n:
    ans += n//c
    c *= 5
print(ans)

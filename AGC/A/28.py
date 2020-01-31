import fractions

n, m = map(int, input().split())
s = input()
t = input()
sr = fractions.gcd(n, m)
sg, tg = n // sr, m // sr
for i in range(sr):
    if s[i * sg] != t[i * tg]:
        print(-1)
        exit()
print(sg * m)

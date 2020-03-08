n = int(input())
a = []
for i in range(n):
    b, c, d, e, f = map(int, input().split())
    t = (b + c + d + e + f * (110 / 900))
    a.append(t)
print(max(a))
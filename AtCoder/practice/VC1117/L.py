n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in range(m):
    b, c = map(int, input().split())
    a.extend([c] * b)

a = sorted(a, reverse=True)
# print(a)

print(sum(a[:n]))

n, l = map(int, input().split())

a = [[] * l for i in range(n)]
for i in range(n):
    I = input()
    for j in range(l):
        a[i].append(I[j])
# print(a)
b = a
for i in range(l-1,-1,-1):
    b = sorted(b, key=lambda x: x[i])

ans = []
for i in range(n):
    ans.append("".join(b[i]))
print("".join(ans))

n = int(input())
s, t = input().split()
a = []
for i, j in zip(s, t):
    a.append(i)
    a.append(j)
print("".join(a))
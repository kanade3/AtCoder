s = input()
a = []
for i in s:
    a.append(i)

a.sort()

print("Yes" if a[0] == a[1] and a[2] == a[3] and a[1] != a[2] else "No")

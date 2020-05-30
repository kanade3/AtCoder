t = str(input())
a = []
for i in range(len(t)):
    if t[i] == '?':
        a.append('D')
    else:
        a.append(t[i])
print("".join(a))

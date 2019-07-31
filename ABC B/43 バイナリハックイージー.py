s = input()
d = 0
m = []
for i in s[::-1]:
    if i == 'B':
        d += 1
    elif d > 0:
        d -= 1
    else:
        m.append(i)

for i in m[::-1]:
    print(i, end='')

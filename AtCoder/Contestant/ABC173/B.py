n = int(input())

a = [0] * 4
t = ['AC', 'WA', 'TLE', 'RE']
for i in range(n):
    s = (input())

    if s == 'AC':
        a[0] += 1
    elif s == 'WA':
        a[1] += 1
    elif s == 'TLE':
        a[2] += 1
    else:
        a[3] += 1

for i in range(4):
    print(t[i], end=' ')
    print('x', end=' ')
    print(a[i])

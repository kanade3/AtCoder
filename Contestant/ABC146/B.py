n = int(input())
s = input()
a = []
for i in s:
    a.append(i)

for i in range(len(a)):
    a[i] = chr((ord(a[i]) + n - 65) % 26 +65)

for i in a:
    print(i, end='')

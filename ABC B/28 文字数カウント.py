S = input()
a = [0] * 6
for i in S:
    a[ord(i) - 65] += 1
for i in range(5):
    print(a[i], end=' ')
print(a[5])

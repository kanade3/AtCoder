n = int(input())
e = 2025 - n
a = []
for i in range(1, int(e ** 0.5) + 1):
    if e % i == 0:
        a.append(i)
        if i != e // i:
            a.append(e // i)
a.sort()
# print(a)
if len(a) == 1:
    print(1, '×', 1)
    exit()
for i in range(len(a)):
    if 1 <= a[i] <= 9 and 1 <= e // a[i] <= 9:
        print(a[i], '×', e // a[i])


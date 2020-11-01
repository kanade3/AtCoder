from collections import Counter

n = input()

C = Counter(n)

if len(n) <= 2:
    if int(n) % 8 == 0 or int(n[::-1]) % 8 == 0:
        print('Yes')
        exit()

for i in range(104, 1000, 8):
    if not Counter(str(i)) - C:
        print('Yes')
        exit()
print('No')

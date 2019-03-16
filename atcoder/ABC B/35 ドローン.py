S = input()
add = 0
T = int(input())
w = S.count('L')
w -= S.count('R')
h = S.count('U')
h -= S.count('D')
q = S.count('?')
if T == 1:
    if w + h >= 0:
        add = q
    else:
        add = -q
else:
    if w + h >= 0:
        add = -q
    else:
        add = q
print(abs(w) + abs(h) + add)

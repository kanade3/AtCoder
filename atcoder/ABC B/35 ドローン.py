S = input()
T = int(input())
w = S.count('L')
w -= S.count('R')
h = S.count('U')
h -= S.count('D')
q = S.count('?')
mix = abs(w) + abs(h)
if T == 1:
    print(mix + q)
else:
    if q > mix:
        print((q-mix) % 2)
    else:
        print(mix - q)

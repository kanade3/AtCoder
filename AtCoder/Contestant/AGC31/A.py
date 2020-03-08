import math


def combinations_count(n, r):
    if n < r:
        return 0
    else:
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


N = int(input())
S = input()
v = [0] * 26
souwa = -1
minus = 0
kaburi = False
for i in range(0, N):
    v[ord(S[i]) - 97] += 1

    souwa += combinations_count(N, i)

    if i >= 2:
        tame = 0
        for j in range(26):
            if v[j] >= 2:
                if i < v[j]:
                    tame += math.factorial(v[j])
                tame += combinations_count(i, v[j])
                print(combinations_count(i, v[j]))

                kaburi = True
        if tame <= combinations_count(N, i):
            souwa -= tame
        else:
            souwa -= combinations_count(N, i)

if not kaburi:
    souwa += 1

print((souwa - minus) % (10 ** 9 + 7))

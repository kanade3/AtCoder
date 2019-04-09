N = int(input())
S = input()
v = [0] * 26
for i in range(0, N):
    v[ord(S[i]) - 97] += 1
wa = 1

for i in range(len(v)):
    wa *= (v[i] + 1)
print((wa - 1) % (10 ** 9 + 7))

# sample code by reud


"""
N = int(input())
S = input()
score = 1
mozis = 'abcdefghijklmnopqrstuvwxyz'
for i in mozis:
    point = S.count(i) + 1
    score *= point

print((score - 1) % (10 ** 9 + 7))

"""

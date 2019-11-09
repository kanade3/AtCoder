n, m = map(int, input().split())
ab = []
h = [1] * m
for i in range(n):
    ai, bi = map(int, input().split())
    ab.append(ai + bi)

cnt = 0
for i in range(len(ab)):
    if i - ab[i] >= 0 and h[i - ab[i]] == 1:
        h[i - ab[i]] = 0
        cnt += 1
print(cnt)
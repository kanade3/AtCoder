n = int(input())
a = list(map(int, input().split()))

d = []
isheld = [0] * 26
for i in range(n):
    b = list(map(int, input().split()))
    d.append(b)
# print(d)

score = 0
minus = 0
for i in range(1, n + 1):
    s = int(input())
    s -= 1

    isheld[s] = i

    for j in range(26):
        score -= a[j] * (i - isheld[j])

    score += d[i - 1][s]
    print(score)

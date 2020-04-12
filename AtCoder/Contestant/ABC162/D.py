n = int(input())

s = input()
cnt = s.count('R') * s.count('G') * s.count('B')

for i in range(n):
    for j in range(n):
        if 0 <= i - j <= i and 0 <= i + j <= n-1:
            x1, x2, x3 = s[i - j], s[i], s[i + j]
            if x1 != x2 and x1 != x3 and x2 != x3:
                cnt -= 1
print(cnt)
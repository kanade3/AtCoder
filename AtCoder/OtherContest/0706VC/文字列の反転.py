x = input()
s = []
for i in x:
    s.append(i)

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    tmp = list(reversed(s[a:b + 1]))

    for j in range(len(tmp)):
        s[a + j] = tmp[j]

print("".join(s))

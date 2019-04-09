s = input()
cnt = 1
a = []
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        cnt += 1
    else:
        a += s[i]
        a += str(cnt)

        cnt = 1
a += s[len(s) - 1]
a += str(cnt)

for i in a:
    print(i, end='')

s = input()
t = input()
cnt = 0
for i in range(len(s) + 1):
    check = ''
    check = s[:i - 1] + s[i::]
    if t == check:
        cnt += 1
print(cnt)

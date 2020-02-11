s = input()
sl = list(s)
t = list(input())
flag = 0
for i in range(len(s) - len(t) + 1):
    cnt = 0
    for j in range(len(t)):
        if s[i + j] != t[j] and s[i + j] != '?':
            break
        else:
            cnt += 1
    if cnt == len(t):
        flag = 1
        index = i

if not flag:
    print('UNRESTORABLE')
else:
    for i in range(len(t)):
        sl[index + i] = t[i]
    for i in range(len(sl)):
        if sl[i] == '?':
            sl[i] = 'a'
    print("".join(sl))

s = list(input())
t = list(input())

flag = True
a = ['a', 't', 'c', 'o', 'd', 'e', 'r']
for i in range(len(s)):
    if s[i] == '@':
        if t[i] in a:
            s[i] = t[i]
    if t[i] == '@':
        if s[i] in a:
            t[i] = s[i]

    if t[i] != s[i]:
        flag = False
print('You can win' if flag else 'You will lose')

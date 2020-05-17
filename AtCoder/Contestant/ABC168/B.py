k = int(input())
s = input()

if len(s) <= k:
    print(s)
else:
    for i in range(len(s)):
        if i < k:
            print(s[i], end='')
        else:
            print('...')
            exit()

s1 = input()
s = s1 + '111111111111'
index = 0
while index < len(s):
    word = s[index:index + 5]
    # print(word)
    if word == '11111':
        break
    if '1' in word:
        print("NO")
        exit()

    if word == 'dream':
        index += 5

        if s[index:index + 2] == 'er':
            if s[index:index + 5] == 'erase':
                pass
            else:
                index += 2

    elif word == 'erase':
        index += 5
        if s[index] == 'r':
            index += 1

    else:
        print('NO')
        exit()

print("YES")

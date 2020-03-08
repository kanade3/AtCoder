s = input()
for i in range(len(s)):
    if i % 2 == 0 and s[i] != 'h':
        print("No")
        exit()
    if i % 2 == 1 and s[i] != 'i':
        print("No")
        exit()
    if len(s) % 2 == 1:
        print("No")
        exit()
print("Yes")

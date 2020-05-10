s = input()
t = input()

if len(s) + 1 != len(t):
    print("No")
else:
    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            exit()
print("Yes")

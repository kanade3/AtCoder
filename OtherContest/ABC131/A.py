s = input()
flag = False
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        flag = True
print("Bad" if flag else "Good")

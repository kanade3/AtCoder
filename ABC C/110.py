s = input()
t = input()

before = [-1] * 26
after = [-1] * 26

for i, j in zip(s, t):
    si = ord(i) - ord('a')
    ti = ord(j) - ord('a')

    if before[si] != -1 or after[ti] != -1:
        if before[si] != ti or after[ti] != si:
            print("No")
            exit()

    before[si] = ti
    after[ti] = si
print("Yes")

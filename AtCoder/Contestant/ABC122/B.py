S = input()

cnt = 0
a = []
for i in range(len(S)):
    if S[i] == 'A' or S[i] == 'T' or S[i] == 'G' or S[i] == 'C':
        cnt += 1
        if i == len(S) - 1:
            a.append(cnt)
    else:
        lenflag = False
        a.append(cnt)
        cnt = 0
print(max(a))
# print(a)

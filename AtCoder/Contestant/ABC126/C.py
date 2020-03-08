S = input()
S += '_'
a = 0
cnt = 0
if S[0] == "0":
    for i in range(0, len(S), 2):
        if S[i] == '1':
            cnt += 1
    for i in range(1, len(S), 2):
        if S[i] == '0':
            cnt += 1
if S[0] == "1":
    for i in range(0, len(S), 2):
        if S[i] == '0':
            cnt += 1
    for i in range(1, len(S), 2):
        if S[i] == '1':
            cnt += 1
print(cnt)

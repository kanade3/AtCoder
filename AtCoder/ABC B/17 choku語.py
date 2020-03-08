x = input()
word = ['o', 'k', 'u']
cnt = 0
for i in range(len(x)):
    if x[i] in word:
        cnt += 1
    elif x[i] == 'c' and x[i + 1] == 'h':
        cnt += 2
print("YES" if cnt == len(x) else 'NO')

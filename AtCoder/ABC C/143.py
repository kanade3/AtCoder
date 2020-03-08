n = int(input())
s = input()
b = s[0]
cnt = 1
for i in range(n):
    if s[i] != b:
        cnt += 1
    b = s[i]
print(cnt)
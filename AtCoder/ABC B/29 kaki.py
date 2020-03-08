s = [(input()) for i in range(12)]
cnt = 0
for i in range(12):
    if "r" in s[i]:
        cnt += 1
print(cnt)

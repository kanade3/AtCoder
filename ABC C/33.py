s = input().split('+')
cnt = 0
for i in s:
    a = i.split('*')
    if '0' not in a:
        cnt += 1

print(cnt)

n = int(input())
for i in range(n):
    s = input()
    cnt = 0
    ans = 0
    flag1 = 0
    for j in range(len(s)):
        if flag1:
            if s[j] == 'L':
                cnt += 1
            else:
                ans = max(ans, cnt + 1)
                flag1 = 0
                cnt = 0

        else:
            if s[j] == 'L':
                cnt += 1
                flag1 = 1
            else:
                cnt = 0

    ans = max(ans, cnt + 1)
    print(ans)

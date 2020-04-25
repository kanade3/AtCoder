t = int(input())

ans_list = []
for i in range(t):
    s = input()
    ans = ""

    for j in range(len(s)):
        if j == 0:
            ans += '(' * int(s[0])
            ans += s[0]
            continue

        elif s[j] < s[j - 1]:
            ans += ')' * (int(s[j - 1]) - int(s[j]))

        else:
            ans += '(' * (int(s[j]) - int(s[j - 1]))

        ans += s[j]

    ans += ')' * int(s[-1])
    ans_list.append(ans)

for i in range(t):
    print("Case #{}:".format(i + 1), end=' ')
    print(ans_list[i])
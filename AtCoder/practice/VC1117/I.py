# https://atcoder.jp/contests/code-festival-2015-morning-easy/tasks/cf_2015_morning_easy_b
n = int(input())
s = input()
ans = 0

if n % 2 != 0:
    print(-1)
    exit()

for i in range(n // 2):
    if s[i] != s[n // 2 + i]:
        ans += 1
print(ans)

# https://atcoder.jp/contests/code-festival-2014-morning-easy/tasks/code_festival_morning_easy_a
n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n - 1):
    ans += a[i + 1] - a[i]
print(ans / (n-1))

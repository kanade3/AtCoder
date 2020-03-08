n = int(input())
x = list(map(int, input().split()))
s = sorted(x)
# print(s)
for i in x:
    print(s[n // 2] if i < s[n // 2] else s[n // 2 - 1])

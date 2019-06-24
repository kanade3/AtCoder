S = input()
al = [0] * 26
make = 0
res = 0

for i in S:
    al[ord(i) - ord('a')] += 1
# print(al)

for i in al:
    make += i // 2 * 2
    res += i % 2

# あまりは一個だけ回文に使う。そのほかは一文字の回文として扱う
if res > 0:
    make += 1
    res -= 1
print(make ** 2 + res)

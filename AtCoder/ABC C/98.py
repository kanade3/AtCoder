n = int(input())
s = input()
# 0ばんめがリーダーのとき方向転換させる人数
e = s.count('E')

w = 0
# 順にみてく
for i in s:
    if i == 'W':
        n = min(n, w + e)
        w += 1
    else:
        w -= 1
        n = min(n, w + e)
print(n)

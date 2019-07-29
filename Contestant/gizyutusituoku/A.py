x, y = map(int, input().split())
flag = True
if y % 2 != 0:
    flag = 0

elif (y / 2 - x) % 2 != 0:
    flag = 0
# 0回でいける時のコーナーケースを見落としていた
print(int(y / 2) if flag and -(y / 2) <= x <= y / 2 and y >= 0 / 2 else '-1')

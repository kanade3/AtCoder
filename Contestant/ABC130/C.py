w, h, x, y = map(int, input().split())
sq = 0
nearX = x - (w / 2)
nearY = y - (h / 2)
flag = False
if (x == 0 and y == 0) or (x == w and y == h) or (x == 0 and y == h) or (x == w and y == 0):
    flag = True

if flag:
    sq = (w*h)/2
    print(str(sq) + ' ' + '0')
    # print('a')
elif nearY < nearX:
    sq = w * (h / 2)
    print(str(sq) + ' ' + '0')
elif nearX < nearY:
    sq = h * (w / 2)
    print(str(sq) + ' ' + '0')
else:
    sq = h * (w / 2)
    print(str(sq) + ' ' + '1')

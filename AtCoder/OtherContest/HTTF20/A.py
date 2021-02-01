from collections import Counter, deque
import random

l = Counter()
location_now = [0, 0]
for i in range(100):
    x, y = map(int, input().split())
    l[i] = [x, y]

print(l)


def is_empty(x, y):
    for v in l.values():
        if v == [x, y]:
            # print([x, y])
            return 0
    return 1


def add_key(now_x, now_y, next_x, next_y):
    if next_x - now_x > 0:
        ans.append('R' * (next_x - now_x))
    else:
        ans.append('L' * (next_x - now_x) * (-1))

    if next_y - now_y > 0:
        ans.append('D' * (next_y - now_y))
    else:
        ans.append('U' * (next_y - now_y) * (-1))


cnt_dist = 0
ans = []
for i in range(20):

    # とりあえず拾う
    for j in range(i, i + 5):
        add_key(location_now[0], l[j][0], location_now[1], l[j][1])
        location_now[0] = l[j][0]
        location_now[1] = l[j][1]
        ans.append('I')

    # 今いる周辺にばらまく
    baramaki_cnt = 0
    while baramaki_cnt < 5:
        rnd_x = random.randint(-3, 3)
        rnd_y = random.randint(-3, 3)
        if location_now[0] + rnd_x < 0 or 19 < location_now[0] + rnd_x or location_now[1] + rnd_y < 0 or 19 < \
                location_now[1] + rnd_y:
            # print(location_now[0] + rnd_x, location_now[1] + rnd_y)
            continue

        add_key(location_now[0], location_now[0] + rnd_x, location_now[1], location_now[1] + rnd_y)
        location_now[0] = location_now[0] + rnd_x
        location_now[1] = location_now[1] + rnd_y

        # print(location_now[0], location_now[1], baramaki_cnt)
        # print(is_empty(location_now[0] + rnd_x, location_now[1] + rnd_y))

        if is_empty(location_now[0], location_now[1]):
            l[i + baramaki_cnt] = [location_now[0], location_now[1]]
            ans.append('O')
            baramaki_cnt += 1
    print(l)
    # 拾う
    for j in range(i, i + 5):
        add_key(location_now[0], l[j][0], location_now[1], l[j][1])
        location_now[0] = l[j][0]
        location_now[1] = l[j][1]
        ans.append('I')

print("".join(ans))
print(len(ans))

e = sorted(list(map(int, input().split())))
b = int(input())
l = sorted(list(map(int, input().split())))

bonus = [0, 0, 0, 0, 0, 0]
cnt = 0
for i in range(6):
    if l[i] in e:
        cnt += 1
        bonus[i] = 1
if cnt == 6:
    print(1)
    exit()
if cnt >= 3:
    prize = 8 - cnt
    # print(bonus.index(0))
    if cnt == 5 and l[bonus.index(0)] == b:
        prize -= 1
    print(prize)
else:
    print(0)

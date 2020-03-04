h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

ans = [[0] * w for i in range(h)]

direction = 'e'

h_now = 0
w_now = 0


def distribute():
    for i in range(n + 1):
        if a[i] > 0:
            a[i] -= 1
            return i + 1


finish = 0
ans[0][0] = 1
a[0] -= 1
while finish <= 4:
    if direction == 'e':
        if w_now + 1 < w and ans[h_now][w_now + 1] == 0:
            w_now += 1
            ans[h_now][w_now] = distribute()
            finish = 0
        else:
            direction = 's'
            finish += 1

    if direction == 's':
        if h_now + 1 < h and ans[h_now + 1][w_now] == 0:
            h_now += 1
            ans[h_now][w_now] = distribute()
            finish = 0
        else:
            direction = 'w'
            finish += 1

    if direction == 'w':
        if w_now - 1 >= 0 and ans[h_now][w_now - 1] == 0:
            w_now -= 1
            ans[h_now][w_now] = distribute()
            finish = 0
        else:
            direction = 'n'
            finish += 1

    if direction == 'n':
        if h_now - 1 >= 0 and ans[h_now - 1][w_now] == 0:
            h_now -= 1
            ans[h_now][w_now] = distribute()
            finish = 0
        else:
            direction = 'e'
            finish += 1
    # print(ans)

for i in range(h):
    for j in range(w):
        print(ans[i][j], end=' ')
    print()

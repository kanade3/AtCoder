H, W, N = map(int, input().split())
t = []
for i in range(H):
    t.append(list(map(int, input().split())))
L = int(input())

a = []
for i in range(L):
    a.append(list(map(int, input().split())))

nokori = H * W
player = [0] * N
turn = 0

for i in range(L):
    # print(player)
    # print(turn)
    if t[a[i][0] - 1][a[i][1] - 1] == t[a[i][2] - 1][a[i][3] - 1]:
        player[turn] += 2
    else:
        turn += 1
        if turn == N:
            turn = 0

for i in range(N):
    print(player[i])

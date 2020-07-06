n, m = map(int, input().split())
box = [1] * n
red = [0] * n
red[0] = 1
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    if box[a]:
        if red[a] == 1:
            red[b] = 1

        if box[a] == 1:
            if red[a] == 1:
                red[a] = 0

        box[a] -= 1
        box[b] += 1

print(sum(red))

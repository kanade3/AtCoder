x, y = map(int, input().split())

for i in range(x + 1):
    s = i
    t = x - i
    # print(s, t)
    if 2 * s + 4 * t == y:
        print('Yes')
        exit()
print("No")

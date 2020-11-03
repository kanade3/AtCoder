while (1):
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        exit()
    key = []
    for i in range(h):
        a = input()
        key.append(a)
    # print(key)

    in_put = input()
    cursorY = 0
    cursorX = 0
    ans = 0
    for i in range(len(in_put)):
        for y in range(h):
            for x in range(w):
                if in_put[i] == key[y][x]:
                    ans += abs(y - cursorY) + abs(x - cursorX)
                    cursorY = y
                    cursorX = x
                    # print(ans)
    print(ans+len(in_put))

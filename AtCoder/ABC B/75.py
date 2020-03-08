h, w = map(int, input().split())
s = []
for i in range(h):
    s.append(input())

y = [0, -1, -1, -1, 0, 1, 1, 1]
x = [1, 1, 0, -1, -1, -1, 0, 1]

for i in range(h):
    for j in range(w):
        cnt = 0
        for m, n in zip(y, x):
            if 0 <= i + m < h and 0 <= j + n < w:
                if s[i + m][j + n] == '#':
                    cnt += 1

        if s[i][j] == '#':
            print('#', end='')
        else:
            print(cnt, end='')
    print()

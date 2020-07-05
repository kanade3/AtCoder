h, w, k = map(int, input().split())
cnt = 0
cntrem = 0
answer = 0
b = []
flag = [[0] * w for _ in range(h)]
for i in range(h):
    b.append(input())
    cnt += b[i].count('#')
# print(cnt)
copy = b
for i in range(2 ** h):
    cntrem = 0
    flag = [[0] * w for _ in range(h)]

    for j in range(h):
        if (i >> j) & 1:
            cntrem += b[j].count('#')

            for roop_w in range(w):
                flag[j][roop_w] = 1
    # print('firstrem', end=' ')
    # print(cntrem)
    tmp = cntrem
    for ka in range(2 ** w):
        cntrem = tmp
        for l in range(w):
            if (ka >> l) & 1:
                for roop_h in range(h):
                    # print(flag)
                    # print(b[roop_h][l])
                    if flag[roop_h][l] == 0 and b[roop_h][l] == '#':
                        cntrem += 1

                # cntrem += b[j].count('#')

        # print(cnt - cntrem)
        if cnt - cntrem == k:
            answer += 1

print(answer)

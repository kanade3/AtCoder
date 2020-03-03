h, w = map(int, input().split())
s = []
for i in range(h):
    s.append(input())


ans_w = [[0] * w for i in range(h)]
ans_h = [[0] * w for i in range(h)]

for i in range(h):
    for j in range(w):
        cnt = 0
        if s[i][j] == '#': continue
        if ans_w[i][j] != 0: continue

        while j + cnt < w:
            if s[i][j + cnt] == '#': break
            cnt += 1

        for k in range(cnt):
            ans_w[i][j + k] = cnt
# print(ans_w)

for i in range(w):
    for j in range(h):
        cnt = 0
        if s[j][i] == '#': continue
        if ans_h[j][i] != 0: continue

        while j + cnt < h:
            if s[j + cnt][i] == '#': break
            cnt += 1

        for k in range(cnt):
            ans_h[j + k][i] = cnt
# print(ans_h)

out = 0
for i in range(h):
    for j in range(w):
        out = max(out, ans_h[i][j] + ans_w[i][j])

print(out - 1)

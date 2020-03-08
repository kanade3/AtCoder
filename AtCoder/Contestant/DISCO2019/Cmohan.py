h, w, k = map(int, input().split())
s, ans, z, a = [], [], [], []
c = 0
for i in range(h):
    #　列
    c += 1
    flag = True
    d = []
    tmp = input()
    # s.append(tmp)
    if tmp == '.' * w:
        # blank
        c -= 1
        ans.append([0] * w)

        # zには0の列が格納される
        z.append(i)

    else:
        # aには0以外の列の値が格納される
        a.append(i)
        for j in range(w):
            if tmp[j] == '#':
                if flag:
                    flag = False
                else:
                    c += 1
            d.append(c)
        ans.append(d)
# flag = True
for i in z:
    # 最初にない場合は後ろのいちごのある列にマージさせる操作
    if i < a[0]:
        ans[i] = ans[a[0]]
    else:
        # その他の場合は前の列にマージ
        ans[i] = ans[i - 1]
print(z)
for i in range(h):
    print(*ans[i])

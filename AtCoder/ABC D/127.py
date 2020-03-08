n, m = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)

z = []
for i in range(m):
    c, d = map(int, input().split())
    z.append([c, d])

z.sort(key=lambda x: x[1], reverse=True)
a_index = 0
z_index = 0
z_num = z[0][0]
ans = 0
# print(a)
# print(z)
flag = 0
for i in range(n):
    if z_num <= 0 and not flag:
        z_index += 1
        if z_index == m:
            flag = 1
        else:
            z_num = z[z_index][0]
    if not flag:
        if z[z_index][1] > a[a_index]:
            z_num -= 1
            ans += z[z_index][1]

        else:
            ans += a[a_index]
            a_index += 1

    else:
        ans += a[a_index]
        a_index += 1

print(ans)

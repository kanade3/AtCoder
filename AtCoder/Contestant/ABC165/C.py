import itertools

n, m, q = map(int, input().split())
a = []
for i in range(q):
    a.append(list(map(int, input().split())))

comb_list = list(itertools.combinations_with_replacement(range(1, m + 1), n))
# print(comb_list)
ans = 0
for i in range(len(comb_list)):
    cnt = 0
    for j in range(q):
        if comb_list[i][a[j][1] - 1] - comb_list[i][a[j][0] - 1] == a[j][2]:
            cnt += a[j][3]
    ans = max(ans, cnt)
print(ans)

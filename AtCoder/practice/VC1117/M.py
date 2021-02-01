# https://atcoder.jp/contests/code-festival-2016-qualc/tasks/codefestival_2016_qualC_b
from collections import Counter

k, t = map(int, input().split())
a = map(int, input().split())

C = Counter(a)
# print(C.most_common()[0])

before_select = -1
ans = 0
for i in range(k):
    select_index, select_value = C.most_common()[0]
    print(C)

    if select_index == before_select:
        C[select_index] = 0
        w = C.most_common()[0]
        if w[1] == 0:
            ans += k - i
            break

    C[select_index] -= 1
    before_select = select_index
print(ans)

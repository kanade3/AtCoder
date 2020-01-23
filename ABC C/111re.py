import collections

n = int(input())
v = list(map(int, input().split()))
v_odd = collections.Counter(v[::2])
v_even = collections.Counter(v[1::2])

if v_odd == v_even and len(v_odd) == 1:
    print(n // 2)
    exit()
if v_odd.most_common()[0][0] != v_even.most_common()[0][0]:
    print(len(v[::2]) - v_odd.most_common()[0][1] + len(v[1::2]) - v_even.most_common()[0][1])
else:
    c1 = len(v[1::2]) - v_even.most_common()[0][1] + len(v[::2]) - v_odd.most_common()[1][1]
    c2 = len(v[1::2]) - v_even.most_common()[1][1] + len(v[::2]) - v_odd.most_common()[0][1]
    print(min(c1, c2))

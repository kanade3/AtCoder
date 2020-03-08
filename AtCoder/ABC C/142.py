import collections

n = int(input())
a = list(map(int, input().split()))

b = collections.OrderedDict()
for i in range(len(a)):
    b[i + 1] = a[i]

c = sorted(b.items(), key=lambda x: x[1])
# print(c)
for i, j in c:
    print(i, end=' ')


"""
別解 numpyのargsortを使う
これはsort後のindexが出力される

In [1]: import numpy as np

In [2]: a = np.array([1, 3, 2])

In [3]: np.argsort(a)
Out[3]: array([0, 2, 1])


解答コード
import numpy as np
N = int(input())
A = list(map(int, input().split()))
 
result = np.argsort(A) + 1
 
print(*result)

argsortについての参照記事
https://deepage.net/features/numpy-sort.html
"""

import heapq
import math
# heapq（優先キュー）は最小値を取り出すのに適しているので、最大値を取り出すためには大小関係を逆転させれば良い。
# そのためにリストの要素を全てに-1をかけている。出力するときに
n, m = map(int, input().split())
a = list(map(int, input().split()))
# a=[-int(j) for j in input().split()] で元のリストから-つきで作れる
b = list(map(lambda x: x * (-1), a))

heapq.heapify(b)
for i in range(m):
    h = heapq.heappop(b)
    heapq.heappush(b, math.ceil(h / 2))

print(sum(b)*(-1))

n = int(input())
xy = []
for i in range(n):
    xy.append(list(map(int, input().split())))

pq = {}

if n == 1:
    print(1)
    exit(0)

for (x, y) in xy:
    for (a, b) in xy:
        if (x, y) != (a, b):
            if (x - a, y - b) in pq.keys():
                # 　x,y座標の差をキーとする連想配列（map）を作成。同じ差のものがあったら+1して、なかったら作る。
                pq[(x - a, y - b)] += 1
            else:
                pq[(x - a, y - b)] = 1

print(n - max(pq.values()))


"""
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
print(xy)
pq = {}

if n == 1:
    print(1)
    exit(0)

for (x, y) in xy:
    for (a, b) in xy:
        if (x, y) != (a, b):
            if (x - a, y - b) in pq.keys():
                pq[(x - a, y - b)] += 1
            else:
                pq[(x - a, y - b)] = 1
print(pq)
print(n - max(pq.values()))
"""

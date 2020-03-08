n, q = map(int, input().split())
node = [0] * (n + 1)

for i in range(n - 1):
    a, b = map(int, input().split())
    node[b] = a

cnt = [0] * (n + 1)

# 何番の親ノードにいくら足されるかがわかる
for _ in range(q):
    p, x = map(int, input().split())
    cnt[p] += x

# この時点ではそれ以下の子ノードに足される所の奴が入ってる
print(cnt)
for i in range(1, n + 1):
    # node[i]はiばんめの親の値が格納されている。
    cnt[i] += cnt[node[i]]

print(node)
print(cnt)
print(cnt[1:])

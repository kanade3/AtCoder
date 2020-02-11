import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
# heapを作成する
heapq.heapify(A)
BC = [list(map(int, input().split())) for _ in range(M)]
BC.sort(key=lambda x: (x[1], x[0]), reverse=True)
print(BC)
for b, c in BC:
    print(b, c)
    if A[0] >= c:
        break
    for i in range(b):
        if A[0] >= c:
            break
        print(A)
        # heappop: popを行い、heapから最小の要素を返す
        heapq.heappop(A)
        print(A, c)
        heapq.heappush(A, c)

print(sum(A))

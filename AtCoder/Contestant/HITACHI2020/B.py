a, b, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = min(A)+min(B)
for i in range(m):
    x, y, d = map(int, input().split())
    cnt = min(cnt, A[x-1] + B[y-1] - d)
print(cnt)

L, H = map(int, input().split())
N = int(input())
a = [int(input()) for i in range(N)]
for i in range(N):
    print(L - a[i] if a[i] < L else -1 if a[i] > H else 0)

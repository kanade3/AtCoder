n, k, s = map(int, input().split())
if s == 10 ** 9:
    for i in range(k):
        print(10**9,end=' ')
    for i in range(n-k):
        print(1,end=' ')

else:
    for i in range(k):
        print(s, end=' ')
    for i in range(n - k):
        print(10 ** 9, end=' ')

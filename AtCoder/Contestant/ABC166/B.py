n, k = map(int, input().split())
b = []
a = []
for i in range(k):
    d = int(input())
    b = list(map(int, input().split()))
    a.extend(b)
print(n-len(set(a)))

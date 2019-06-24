n = int(input())
w = [int(i) for i in input().split()]
p = 100000
a = sum(w)
k = 0
for i in range(n - 1):
    k += w[i]
    p = min(p, abs(k - (a - k)))
print(p)

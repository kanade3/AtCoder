n, k, q = map(int, input().split())
a = [k - q] * n
for i in range(q):
    a_in = int(input())
    a[a_in - 1] += 1

for i in range(n):
    print('Yes' if a[i] > 0 else 'No')

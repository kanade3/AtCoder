n = int(input())
h = list(map(int, input().split()))
flag = True
for i in range(n-1, 1, -1):
    if h[i] - h[i - 1] < 0:
        h[i - 1] -= 1
        if h[i] - h[i - 1] < 0:
            flag = 0
if h[0] > h[-1]:
    flag = 0

# print(h)
print("Yes" if flag else 'No')

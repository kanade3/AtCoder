n = int(input())
v = list(map(int, input().split()))
v.sort()

for i in range(1, n):
    # print(i)
    if i == n - 1:
        print(sum(v) / 2)
        exit()
    v[i] = (v[i] + v[i - 1]) / 2
    v[i-1]=0

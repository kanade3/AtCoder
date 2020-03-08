N = int(input())
a = [int(input()) for i in range(N)]
b = []
for i in range(N):
    b.append([a[i], i])
b.sort(key=lambda x: x[0])

# print(b)
for i in range(N):
    if i != b[-1][1]:
        print(b[-1][0])
    else:
        print(b[-2][0])

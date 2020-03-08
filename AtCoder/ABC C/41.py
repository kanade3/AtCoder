n = int(input())
a = list(map(int, input().split()))
b = []
index = 1
for i in a:
    b.append([i, index])
    index += 1
b.sort(reverse=True, key=lambda x: x[0])
for i, j in b:
    print(j)

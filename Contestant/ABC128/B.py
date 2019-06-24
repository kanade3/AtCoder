N = int(input())
a = []

for i in range(N):
    x, y = map(str, input().split())
    a.append([x, int(y), i + 1])

a.sort(key=lambda x: x[1], reverse=True)
a.sort(key=lambda x: x[0])

for i in a:
    print(i[2])

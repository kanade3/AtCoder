c = int(input())
a = []
for i in range(c):
    b = sorted(map(int, input().split()), reverse=True)
    a.append(b)

ans=1
for i in range(c):
    tmp=0
    for j in range(3):
        tmp=max()
a, b = map(int, input().split())

if a != b:
    for i in range(max(a,b)):
        print(min(a, b),end='')
else:
    for i in range(a):
        print(b,end='')

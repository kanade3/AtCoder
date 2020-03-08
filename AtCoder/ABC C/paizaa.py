n, x = map(int, input().split())
a = [int(input()) for i in range(n)]
b = list(bin(x))
for i in a:
    print(b[len(b)-i])

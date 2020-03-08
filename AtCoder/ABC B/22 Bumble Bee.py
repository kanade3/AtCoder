N = int(input())
a = [int(input()) for i in range(N)]
b=set(a)
print(len(a)-len(b))

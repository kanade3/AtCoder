n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(a) > sum(b):
    print('A1')
elif sum(a) < sum(b):
    print('B')
else:
    print('same')

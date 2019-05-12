N = int(input())
a = [int(i) for i in input().split()]
cnt = 0
s = 0
smallest = 10000000000
for i in range(len(a)):
    if a[i] < 0:
        cnt += 1

    smallest = min(abs(a[i]), smallest)
    s += abs(a[i])

if cnt % 2 == 0:
    print(s)
else:
    print(s - 2 * smallest)
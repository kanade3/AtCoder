n = int(input())
a = list(map(int, input().split()))

num = 0
tmp = a[0]
sub_num=0

for i in range(1, n):

    if tmp < a[i]:
        sub_num += 1
        num += sub_num

    else:
        sub_num = 0
    tmp = a[i]
print(num+n)

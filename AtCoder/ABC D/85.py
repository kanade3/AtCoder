import math

n, h = map(int, input().split())
A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A.sort(reverse=True)
B.sort(reverse=True)

cnt = 0
cnt_num = 0
for i in range(n):
    if B[i] < A[0]:
        break
    cnt += B[i]
    cnt_num += 1
    if cnt >= h:
        print(i + 1)
        exit()

left = h - cnt
print(math.ceil(left / A[0]) + cnt_num)

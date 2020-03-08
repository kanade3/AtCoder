import bisect

n, m = map(int, input().split())
x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

time_cnt = 0
cnt = 0

while 1:
    a_index = bisect.bisect_left(a, time_cnt)
    if a_index >= n:
        break

    time_cnt = a[a_index] + x

    b_index = bisect.bisect_left(b, time_cnt)

    if b_index >= m:
        break

    time_cnt = b[b_index] + y
    cnt += 1

print(cnt)

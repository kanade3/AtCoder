n, m = map(int, input().split())
short = n
if short > 12:
    short = n - 12
long = m
arg_long = long * 6
arg_short = 0.5 * long + short * 30

# print(arg_long,arg_short)
ans = abs(arg_long - arg_short)
print(min(ans, 360 - ans))

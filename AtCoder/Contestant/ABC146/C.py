a, b, x = map(int, input().split())
low, high = 0, 10 ** 11
while low + 1 < high:
    mid = (high + low) // 2
    c = a * mid + b * len(str(mid))

    if c <= x:
        low = mid
    else:
        high = mid

print(low if low <= 10 ** 9 else 10 ** 9)

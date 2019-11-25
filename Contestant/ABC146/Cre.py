a, b, x = map(int, input().split())
low, high = 0, 10 ** 10

while low + 1 < high:
    mid = (low + high) // 2

    if a * mid + b * len(str(mid)) <= x:
        low = mid
    else:
        high = mid
print(low if low < 10 ** 9 else 10 ** 9)

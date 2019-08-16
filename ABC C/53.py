x = int(input())
s = x // 11
print(2 * s if x % 11 == 0 else 2 * s + 1 if x % 11 <= 6 else 2 * s + 2)

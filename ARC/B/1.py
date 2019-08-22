a, b = map(int, input().split())
r = [0, 1, 2, 3, 2, 1, 2, 3, 3, 2]
print(abs(b - a) // 10 + r[abs(b - a) % 10])

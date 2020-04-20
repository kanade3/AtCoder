n, m = map(int, input().split())
a = list(map(int, input().split()))

p = sum(a)

print(n - p if n - p >= 0 else -1)

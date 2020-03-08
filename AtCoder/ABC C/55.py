n, m = map(int, input().split())
restC = m - n * 2
print(n + restC // 4 if restC >= 0 else m//2)

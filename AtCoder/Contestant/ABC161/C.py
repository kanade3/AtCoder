n, k = map(int, input().split())
w = n // k
q = -(-n // k)
print(min(abs(n - (w * k)), abs(n - (q * k))))

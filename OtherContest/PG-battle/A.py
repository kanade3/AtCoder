w, k, d = map(int, input().split())

print("Yes" if k <= d and w - k <= d else "No")

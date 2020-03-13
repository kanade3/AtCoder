n = int(input())

for i in range(n):
    r = int(input())
    a = list(map(int, input().split()))
    d = max(a)
    ok = True
    for j in range(r):
        if (max(a) - a[j]) % 2 != 0:
            ok =False
    print("YES" if ok else "NO")

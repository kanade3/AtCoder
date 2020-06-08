n, m = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)
b = sorted(list(map(int, input().split())), reverse=True)
if len(b) > len(a):
    print("NO")
    exit()

for i in range(len(b)):
    if a[i] < b[i]:
        print('NO')
        exit()
print("YES")

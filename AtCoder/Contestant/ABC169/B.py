
n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)

cnt = 1
if 0 in a:
    print(0)
    exit()

for i in range(len(a)):
    cnt *= a[i]
    if cnt > 10 ** 18:
        print(-1)
        exit()
print(cnt)

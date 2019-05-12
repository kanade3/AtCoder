n, k = map(int, input().split())
cnt = 0
for i in range(n):
    if i + k >= n:
        print(cnt + 1)
        break
    else:
        cnt += 1
print(cnt)

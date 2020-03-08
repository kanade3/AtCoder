n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in a:
    if i % 6 == 2 or i == 4:
        cnt += 1
    elif i % 6 == 5:
        cnt += 2
    elif i % 6 == 0:
        cnt += 3

print(cnt)

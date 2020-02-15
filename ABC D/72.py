n = int(input())
p = list(map(int, input().split()))

index = 0
cnt = 0
while index < n:
    if p[index] == index + 1:
        cnt += 1
        index += 2
    else:
        index += 1
print(cnt)

n = int(input())
a = list(map(int, input().split()))
cnt4 = 0
cnt2 = 0
for i in a:
    if i % 4 == 0:
        cnt4 += 1
    elif i % 2 == 0:
        cnt2 += 1
if cnt2 == 0:
    cnt2 = 1
print("Yes" if cnt4 >= (n - (cnt2 - 1)) // 2 else 'No')

n = int(input())
cnt = 0
if n % 2 == 0:
    cnt = n // 2
else:
    cnt = n // 2 + 1
print(cnt / n)

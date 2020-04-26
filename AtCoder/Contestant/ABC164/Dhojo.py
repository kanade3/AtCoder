a = int(input())
cnt = 0
for i in range(1, 2 * 10 ** 6 + 2):
    if i % 3 == 0 and i % 673 == 0:
        cnt += 1

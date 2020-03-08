n = int(input())
s = input()
index = 0
cnt = 0
for i in range(0, 1000):
    if i < 10:
        value = '00' + str(i)
    elif i < 100:
        value = '0' + str(i)
    else:
        value = str(i)

    for j in s:
        if value[index] == j:
            index += 1

        if index == 3:
            cnt += 1
            index = 0
            break
    index = 0

print(cnt)

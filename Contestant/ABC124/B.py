a = [float(input()) for i in range(5)]
sum = 0
amari = 10
index = 0
for i in range(5):
    if a[i] % 10 < amari and a[i] % 10 != 0:
        index = i
        amari=a[i] % 10
        # print(index)
# print(index)
for i in range(5):
    if i == index:
        pass
    else:
        if a[i] % 10 != 0:
            sum += a[i]+10 - a[i] % 10
        else:
            sum += a[i]
sum += a[index]
print(int(sum))

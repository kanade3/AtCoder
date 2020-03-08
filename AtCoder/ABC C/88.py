a = []
for i in range(3):
    a.append(list(map(int, input().split())))

for m in range(101):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if a[i][j] == m:
                cnt += 1
                print(1)
    print('/')
    if cnt == 9:
        print("Yes")
        exit()
print("No")

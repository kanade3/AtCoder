n=int(input())
a=sorted(list(map(int,input().split())))

x=a[0]
for i in range(1,len(a)):
    if x==a[i]:
        print('NO')
        exit()
    else:
        x=a[i]
print("YES")
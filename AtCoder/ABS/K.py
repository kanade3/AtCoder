n = int(input())
a=[]
for i in range(n):
    t,x,y = map(int,input().split())
    a.append([t,x,y])

now = 0
now_x,now_y=0,0
ok = True
for i in range(n):
    time = a[i][0] - now
    now = a[i][0]
    cost = abs(a[i][1]-now_x)+abs(a[i][2]-now_y)
    now_x, now_y = a[i][1],a[i][2]
    if time < cost:
        ok =False
        break
    elif (time - cost) %2 !=0:
        ok =False
        break
print("Yes" if ok else "No")

k,x=map(int,input().split())

xm=x-(k-1)
xl=x+(k-1)
for i in range(xm,xl+1):
    print(i,end=' ')

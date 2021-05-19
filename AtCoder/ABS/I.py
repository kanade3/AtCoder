n,y=map(int,input().split())
for i in range(n+1):
    for j in range(n+1):
        k = n-i-j
        if k<0:
            continue
        if i*1000+j*5000+k*10000 == y:
            print(k,j,i)
            exit()
print(-1,-1,-1)
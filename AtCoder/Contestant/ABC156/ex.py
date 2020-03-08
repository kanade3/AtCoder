P=int(input())
X=list(map(int,input().split()))
l=[]
mini=10000000000000000000000
for j in range(min(X),max(X)):
    ans = [(i-j)**2 for i in X ]
    if sum(ans)<mini:
        mini = sum(ans)
print(mini)
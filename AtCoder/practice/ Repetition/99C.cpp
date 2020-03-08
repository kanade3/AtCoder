#include <bits/stdc++.h>
#define rep(i,n) for (int i=0;i<(n);++i)
using namespace std;
using ll = long long;

ll INF = 10000000000;
int dp[100020];

int main()
{
    int N; cin>>N;
    rep(i,N+1) dp[i]=1e9;
    dp[0]=0;
 
    rep(i,N){
        for(int j=1;i+j<=N;j*=6) 
            dp[i+j]=min(dp[i+j],dp[i]+1);
        for(int j=1;i+j<=N;j*=9)
            dp[i+j]=min(dp[i+j],dp[i]+1);
    }
    cout<<dp[N]<<endl;
}
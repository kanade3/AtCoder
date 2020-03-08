#include <bits/stdc++.h>
#define rep(i,n) for (int i=0;i<(n);++i)
using namespace std;
using ll = long long;

int dp[105][4][2];

int main(){
    string s;
    cin >> s;
    int n=s.size();
    cin >> n;
    int K;
    cin >> K;
    dp[0][0][0]=1;
    // dp[i][j][k]はi桁目まで決めた時j個の非ゼロを使ってそこまでの桁が入力と一致するかを確かめる。
    // kはそこまでの桁数が一致していないなら1。そのあとは1~9までなんでもOK。
    rep(i,n)rep(j,4)rep(k,2){
        int nd = s[i]-'0';
        rep(d,10){
            int ni=i,nj=j,nk=k;
            if (d!=0)nj++;
            if (nj>K)continue;
            
            // 桁数一致でk==0
            if (k==0){
                // d=ndの時は桁数が一致するので、次に判断を委ねる
                if (d>nd)continue;
                if (d<nd) nk=1;
            }
            dp[ni][nj][nk]+=dp[i][j][k];
        }
    }
    ll ans = dp[n][K][0] + dp[n][K][1];
    cout << ans << endl;
}
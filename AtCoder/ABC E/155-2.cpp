#include <bits/stdc++.h>
#define rep(i,n) for (int i=0;i<(n);++i)
using namespace std;
using ll = long long;
using P = pair<int,int>;

const int INF = 1001001001;
int dp[100005][2];

int main(){
    string s;
    cin >> s;
    // 筆算のように下の桁から計算を行う
    reverse(s.begin(), s.end());
    // 下の桁から考えるかもなので。
    s += '0';
    int n = s.size();
    rep(i,n+1)rep(j,2) dp[i][j]=INF;
    dp[0][0]=0;

    rep(i,n)rep(j,2){
        int x = s[i]-'0';
        // 繰り下がり
        x += j;
        rep(a,10){
            // 遷移先の状態
            int ni = i+1 , nj =0;
            int b = a-x;
            if (b<0){
                // 繰り下がり要因
                nj = 1;
                b += 10;
            }
            dp[ni][nj] = min(dp[ni][nj], dp[i][j]+a+b);
        }
    }
    // 最後繰り下がりがあってはいけないので、dp[n][0]を出力する
    int ans = dp[n][0];
    cout << ans << endl;
    return 0;

}
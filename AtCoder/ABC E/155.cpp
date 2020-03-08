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
    // 下の桁のから行う
    reverse(s.begin(), s.end());
    //下の桁から考えることもあるので（繰り上がり）0を付け加えておく
    // 1234 >> 43210 最後の桁に0をつけている??
    s += '0';
    int n = s.size();
    rep(i,n+1)rep(j,2) dp[i][j]= INF;
    dp[0][0] = 0;

    
    rep(i,n)rep(j,2) {
        int x = s[i] - '0';
        //　繰り下がりの処理 お金は多く払ってもいいから一番大きい桁の繰り下がりも考えて良い。
        x += j;
        rep(a,10){
            // 遷移先の状態
            int ni = i+1, nj = 0;
            int b = a-x;
            // 0以下になったら上の桁から借りる
            if (b < 0){
                nj = 1;
                b += 10;
            }
            // dpは硬貨の枚数でやっていることに注意しよう。
            dp[ni][nj] = min(dp[ni][nj], dp[i][j]+a+b);
        }
    }
    // 最後繰り下がりがあってはいけないのでdp[n][0]を出力する
    int ans = dp[n][0];
    cout << ans << endl;
    return 0;
}
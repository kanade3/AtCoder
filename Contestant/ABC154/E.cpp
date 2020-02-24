#include <bits/stdc++.h>
#define rep(i,n) for (int i=0;i<(n);++i)
using namespace std;
using ll = long long;

int dp[105][4][2];

int main(){
    string s;
    cin >> s;
    int n = s.size();
    int K;
    cin >> K;
    dp[0][0][0]=1;
    // dp[i][j][k]はi桁目まで決めた時、j個の非ゼロを用いてkはそこまでの桁数がNと一致するかどうかを確かめる
    // 例310942で一番左が2の時はni=1,nj=1,nk=1
    // 同じ例で一番左が3の時はni=1,nj=1,nk=0
    // 一番左が5の時は遷移させちゃダメ。なのでcontinue
    rep(i,n)rep(j,4)rep(k,2){
        // 文字列で格納して文字列の'0'をひいて数字にしているところがポイント
        int nd = s[i]-'0';
        rep(d,10){
            int ni=i+1,nj=j,nk=k;
            if (d!=0)nj++;
            if (nj>K)continue;
            // 桁数が一致しているときはk==0
            if (k==0){
                // 次の数字でnkを判断。d=ndの場合はまだ桁数が一致するので次に判断を委ねる。
                if(d > nd) continue;
                if(d < nd) nk=1;
            }
            dp[ni][nj][nk]+=dp[i][j][k];
        }
    }
    // 桁数一致の0と桁数一致していない1を足し合わせる。
    ll ans = dp[n][K][0] + dp[n][K][1];
    cout << ans << endl;
}
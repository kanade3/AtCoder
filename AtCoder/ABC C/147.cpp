#include <bits/stdc++.h>
#define rep(i,n) for (int i=0;i<(n);++i)
using namespace std;
using ll = long long;

int g[15][15];
int main(){
    int n;
    cin>> n;
    // iばんめの人がjばんめの人をどう言ったかが格納されている。-1は未定義
    rep(i,n)rep(j,n)g[i][j]=-1;
    rep(i,n){
        int m;
        cin >>m;
        rep(j,m){
            int a,x;
            cin>>a>>x;
            // indexを揃える
            --a;
            g[i][a]=x;
        }
    }
    // 入力終わり
    int ans=0;
    // bit全探索で、iさんを正直者と見立てることをすべてのパターンで試す。
    rep(i,1<<n){
        vector<int>d(n);
        // 1が立っているところを正直者として格納する。iのjビット目が1かどうかを判断
        rep(j,n) if (i>>j&1){
            d[j]=1;
        }
        bool ok=true;
        rep(j,n){
            // 正直者だと割り当てをした人がいたら証言をすべてチェックする
            if (d[j]){
                rep(k,n){
                    if (g[j][k] == -1)continue;
                    if (g[j][k]!= d[k]) ok = false;
                }
            }
        }
        // iが立っているビットの数をカウントする
        if (ok) ans = max(ans,__builtin_popcount(i));
    }
    cout << ans<<endl;
}
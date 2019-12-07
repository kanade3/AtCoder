#include <bits/stdc++.h>
#define rep(i,n) for (int i=0 ;i < (n); ++i)
using namespace std;

int main(){
    int n,m;
    cin >> n >> m;
    vector <int> k(m);
    // 先に二次元配列を作っておく
    int s[10][10];
    vector <int> p(m);
    rep(i,m){
        // kにはi番目のランプに何個のボタンがあるかが格納される
        cin >> k[i]; 
        rep(j,k[i]){
            cin >>s[i][j];
            s[i][j]--;
        }
    }

    rep(i,m){
        cin >> p[i];
    }
    int ans=0;
    // n以下全探索（n bit左シフトすることで全通りのビット演算を行うことができる。)
    rep (i,1<<n){
        int flag=1;
        rep(j,m){
            int cnt=0;
            rep(h ,k[j]){
                printf("%d",i);
                cout << endl;
                // ビットをcolumnごとに調べて、その電球に対応するスイッチが何個点灯しているかを確かめる
                cnt+=(i>>s[j][h])&1;
            }
            // 上の計算で求めたcntを元に、2で割った余りによって点灯かどうかを判断。全部ついてなかったらアウト。
            if(cnt%2!=p[j]){
                flag=0;
            }
        }
        // 全部ついていたらansを増やす
        if(flag){
            ans++;
        }
    }
    cout << ans << endl ;

    return 0;
}
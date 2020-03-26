#include <bits/stdc++.h>
#define rep(i,n) for (int i=0;i<(n);++i)
using namespace std;
using ll = long long;

const int INF = 1001001001;
int c[10][1005];

int main(){
    int h, w, k;
    cin >> h >> w >> k;

    vector<string>s(h);
    rep(i,h) cin >> s[i];
    int ans = INF;

    // bit全探索
    rep(div,1<<(h-1)){
        int g = 0 ;
        vector<int> id(h);
        // groupを作る。bitが立ってたらグループを追加する
        rep(i,h){
            id[i]=g;
            if (div>>i&1) ++g;
        }

        ++g;
        // groupは0で初期化しておく。
        rep(i,g)rep(j,w) c[i][j] = 0;
        rep(i,h)rep(j,w) c[id[i]][j] += (s[i][j]-'0');

        int num = g-1;
        vector<int> now(g);
        // 無名関数を定義して、グループに属すことができるかどうかを判断する
        // &を指定することで関数の範囲外のものにアクセスすることができる。
        auto add = [&](int j){
            rep(i,g) now[i] += c[i][j];
            rep(i,g) if (now[i] > k) return false;
            return true;
        };

        rep(j,w){
            if (!add(j)){
                num++;
                now = vector<int>(g);
                if (!add(j)){
                    num = INF;
                    break;
                }
            }
        }
        ans = min(ans,num);
    }
    cout << ans << endl;
    return 0;
}
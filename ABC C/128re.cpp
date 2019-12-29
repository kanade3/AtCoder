#include <bits/stdc++.h>
#define rep(i,n) for (int i=0 ;i < (n); ++i)
using namespace std;

int main(){
    int N,M;
    int ans=0;
    cin >> N >> M;
    vector<int> a(N);
    rep(i,M){
        int k;
        cin >> k;
        rep(j,k){
            int s;
            cin >> s;
            a[s] |= 1<<i;
        }
    }
    int p=0;
    rep(i,M){
        int x;
        cin >>x;
        p |= x<<i;
    }

    rep(s,1<<N){
        // 実際にどの電球がついているかを格納
        int t=0;
        rep(i,N){
            // i bit目が立っているかを判断する
            if(s>>i&1){
                // 立っていたら押すとアクションするよ。
                t^=a[i];
            }
        }
        if(t==p){
            ans++;
        }

    }
    cout << ans << endl;

}

/*
index揃えるために(0 base index)s--でデクリメントしている。
|= はor=で、rep jのループ(k個のスイッチ)をi bit左シフトしor=をとっている。
これでs番目の電球にはどのスイッチがついているかがわかる。

rep kループが終わったらスイッチの押し方を全部試す。
1<<N でN bit目よりしたの全ての組み合わせが試せる。
pでは電球が0 or 1 で点灯するかどうかが格納される
*/
#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using ll = int64_t;
#define REP(i, n) for(ll (i) = 0; (i) < (n); ++(i))
#define REPR(i, n) for(ll (i) = (n); (i) >= 0; --(i))
#define FOR(i, n, m) for(ll (i) = (n); (i) < (m); ++(i))
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return true; } return false; }
template<class T>bool chmin(T &a, const T &b) { if (a>b) { a=b; return true; } return false; }

int main(){
    ll N,C;
    cin >> N >> C;
    vector<pair<ll,ll>> event;
    REP(i,N){
        ll a,b,c;
        cin >> a >> b >> c;
        // a-1日が終わるとc円上がり、b日が終わるとc円下がる
        event.emplace_back(a-1,c);
        event.emplace_back(b,-c);
    }
    
    sort(event.begin(),event.end());
    ll ans = 0 , fee = 0 , t = 0;
    for (auto [x,y] : event){
        if (x != t){
            ans += min(C,fee) * (x-t);
            t = x;
        }
        fee += y;
    }
    cout << ans << endl;
}

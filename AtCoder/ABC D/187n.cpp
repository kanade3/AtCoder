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
    int N;
    cin >> N;
    ll A;
    vector<ll> s(N);
    REP(i,N){
        ll a,b;
        cin >> a >> b;
        A -= a;
        s[i]= 2 * a + b;
    }
    sort(s.begin(),s.end());
    ll ans = 0;
    while(A<=0){
        A += s.back();
        s.pop_back();
        ans++;
    }
    cout << ans << endl;
}
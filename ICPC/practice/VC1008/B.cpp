#include <bits/stdc++.h>
using namespace std;

#define REP(i, n) for(int (i) = 0; (i) < (n); ++(i))
#define REPR(i, n) for(int (i) = (n); (i) >= 0; --(i))
#define FOR(i, n, m) for(int (i) = (n); (i) < (m); ++(i))
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return true; } return false; }

int x,y,s;
void solve(){
    int a,b;
    int ans = -1;
    REP(i,s){
        REP(j,s){
            if(i==0 || j==0)continue;
            if(i * (100+x)/100 + j * (100+x)/100 == s){
                ans = max(ans, i * (100+y)/100 + j * (100+y)/100);
            }
        }
    }
    cout << ans << endl;
}
int main(){
    while(1){
        cin >> x >> y >> s;
        if(x==0 && y==0 &&s==0) return 0;
        solve();
    }
}
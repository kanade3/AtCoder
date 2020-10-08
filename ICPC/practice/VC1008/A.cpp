#include <bits/stdc++.h>
using namespace std;

#define REP(i, n) for(int (i) = 0; (i) < (n); ++(i))
#define REPR(i, n) for(int (i) = (n); (i) >= 0; --(i))
#define FOR(i, n, m) for(int (i) = (n); (i) < (m); ++(i))
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return true; } return false; }

int m,nmin,nmax;
vector<int>a;

void solve(){
    int diff=-1;
    int ans;

    for(int i=nmin;i<=nmax;i++){
        if(diff <= a[m-i] - a[m-i-1]){
            ans = i;
            diff = a[m-i] - a[m-i-1];
        }
    }
    cout << ans << endl;
}

int main(){
    while(1){
        cin >> m >> nmin >> nmax;
        a.resize(m);
        if(m==0 && nmin==0 && nmax==0) return 0;
        REP(i,m){
                cin >> a[i];
            }

        sort(a.begin(), a.end());
        solve();
    }
}
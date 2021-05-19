#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define REP(i, n) for (int(i) = 0; (i) < (n); ++(i))
#define REPR(i, n) for (int(i) = (n); (i) >= 0; --(i))
#define FOR(i, n, m) for (int(i) = (n); (i) < (m); ++(i))

int main(){
    int a,b,c,x,ans;
    ans = 0;
    cin>>a>>b>>c>>x;
    REP(i,a+1) REP(j,b+1) REP(k,c+1) if(i*500+j*100+k*50 == x)ans++;
    cout << ans << endl;
}
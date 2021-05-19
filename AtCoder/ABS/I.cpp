#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define REP(i, n) for (int(i) = 0; (i) < (n); ++(i))
#define REPR(i, n) for (int(i) = (n); (i) >= 0; --(i))
#define FOR(i, n, m) for (int(i) = (n); (i) < (m); ++(i))
int main(){
    int n,y,k;
    cin >> n >> y;
    REP(i,n+1)REP(j,n+1){
        k = n - i - j;
        if(k<0)continue;
        if(i*10000 +j*5000 + k*1000==y){
            cout<< i << ' ' << j << ' ' << k << endl;
            return 0;
        }
    }
    cout << -1 << ' ' << -1 << ' ' << -1 << endl;
    return 0;
}
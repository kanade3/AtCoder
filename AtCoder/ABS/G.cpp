#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define REP(i, n) for (int(i) = 0; (i) < (n); ++(i))
#define REPR(i, n) for (int(i) = (n); (i) >= 0; --(i))
#define FOR(i, n, m) for (int(i) = (n); (i) < (m); ++(i))

int main(){
    int n,res_a,res_b;
    res_a = 0;
    res_b = 0;
    cin >> n;
    vector<int>a(n);
    REP(i,n) cin >> a[i];
    sort(a.rbegin(),a.rend());
    REP(i,n){
        if(i%2==0){
            res_a+=a[i];
        }
        else{
            res_b+=a[i];
        }
    }
    cout << res_a - res_b << endl;
}

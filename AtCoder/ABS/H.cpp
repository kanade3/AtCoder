#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define REP(i, n) for (int(i) = 0; (i) < (n); ++(i))
#define REPR(i, n) for (int(i) = (n); (i) >= 0; --(i))
#define FOR(i, n, m) for (int(i) = (n); (i) < (m); ++(i))

int main(){
    int n;
    cin >> n;
    vector<int>a(n);
    REP(i,n) cin >> a[i];
    set<int> s(a.begin(),a.end());
    cout << s.size() << endl;
}
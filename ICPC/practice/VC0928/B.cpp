#include <bits/stdc++.h>
using namespace std;

#define REP(i, n) for(int (i) = 0; (i) < (n); ++(i))
#define REPR(i, n) for(int (i) = (n); (i) >= 0; --(i))
#define FOR(i, n, m) for(int (i) = (n); (i) < (m); ++(i))
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return true; } return false; }

int main(){
    while(true){
        int N;
        int ans = 1000000;
        vector<int>a;

        cin >>N;
        a.resize(N);
        if(N==0) return 0;

        REP(i,N){
            cin >> a[i];
        }
        sort(a.begin(), a.end());
        
        REP(i,N-1){
            if(a[i+1]-a[i] < ans){
                ans = a[i+1] - a[i];
            }
        }
        cout << ans << endl;
    }
    return 0;
}
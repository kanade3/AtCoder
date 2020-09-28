#include <bits/stdc++.h>
using namespace std;

#define REP(i, n) for(int (i) = 0; (i) < (n); ++(i))
#define REPR(i, n) for(int (i) = (n); (i) >= 0; --(i))
#define FOR(i, n, m) for(int (i) = (n); (i) < (m); ++(i))
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return true; } return false; }

int main(){
    while(true){
        int n,m;
        int ans = 0;
        cin >> n >> m;
        if(n==0 && m==0){
            return 0;
        }
        vector<int>a(n);
        REP(i,n){
            cin >> a[i];
        }
        REP(i,n){
            REP(j,n){
                if(i==j){
                    continue;
                }
                int s = a[i] + a[j];
                if(s> ans && s<=m){
                    ans = s;
                }
            }
        }
        if(ans==0){
            cout << "NONE" << endl;
        }
        else{
            cout << ans << endl;
        }
        ans = 0;
    }
    return 0;
}
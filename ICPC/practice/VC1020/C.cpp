#include <bits/stdc++.h>
using namespace std;

#define REP(i, n) for(int (i) = 0; (i) < (n); ++(i))
#define REPR(i, n) for(int (i) = (n); (i) >= 0; --(i))
#define FOR(i, n, m) for(int (i) = (n); (i) < (m); ++(i))
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return true; } return false; }

int n,p;
void solve(){
    vector<int> c(n,0);
    int index = 0;
    int pot = p;
    while(1){
        if(pot==0){
            auto res = find(c.begin(), c.end(), p);
            if(res!=c.end()){
                cout << distance(c.begin(), res) << endl;
                return;
            }
        }
        if(pot){
            pot--;
            c[index]++;
        }else{
            pot+=c[index];
            c[index]=0;
        }
        index++;
        index%=n;
    }
}

int main(){
    while(cin >> n >> p, n != 0 && p != 0) {
        solve();
    }
}
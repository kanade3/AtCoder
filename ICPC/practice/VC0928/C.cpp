#include <bits/stdc++.h>
using namespace std;

#define REP(i, n) for(int (i) = 0; (i) < (n); ++(i))
#define REPR(i, n) for(int (i) = (n); (i) >= 0; --(i))
#define FOR(i, n, m) for(int (i) = (n); (i) < (m); ++(i))
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return true; } return false; }


int n;

void solve(){
    vector<char> c(n);
    vector<int> cnt(26,0);
    REP(i,n){
        cin >> c[i];
    }
    REP(i,n){
        cnt[c[i]-'A']++;

        int max_index,max_num = -1;
        REP(i,26){
            if(max_num < cnt[i]){
                max_num = cnt[i];
                max_index = i;
            }
        }
        int second_index,second_num = -1;
        REP(i,26){
            if(i == max_index) continue;

            if(second_num < cnt[i]){
                second_num = cnt[i];
                second_index = i;
            }
        }
        if(second_num + (n-(i+1)) < max_num){
            cout << char(max_index+'A') << " " << i+1 << endl;
            return;
        }
    }
    cout << "TIE" << endl;
}

int main(){
    while(1){
        cin >> n;
        if(n==0) break;
        solve();
    }
    return 0 ;

}
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define REP(i, n) for (int(i) = 0; (i) < (n); ++(i))
#define REPR(i, n) for (int(i) = (n); (i) >= 0; --(i))
#define FOR(i, n, m) for (int(i) = (n); (i) < (m); ++(i))

int main(){
    int n,t,x,y;
    cin >> n;
    vector<vector<int>> vv;
    REP(i,n){
        cin >> t >> x >> y;
        vv.push_back({t,x,y});
    }
    int time,now=0,cost=0,now_x=0,now_y=0;
    bool ok = true;
    REP(i,n){
        time = vv[i][0] - now;
        now = vv[i][0];
        cost = abs(now_x-vv[i][1]) + abs(now_y-vv[i][2]);
        now_x = vv[i][1];
        now_y = vv[i][2];
        if(time-cost<0 || (time-cost) %2 !=0){
            ok = false;
            break;
        }
    }
    if(ok){
        cout << "Yes" << endl;
    }
    else{
        cout << "No" << endl;
    }
}
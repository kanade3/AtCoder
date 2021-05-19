#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define REP(i, n) for (int(i) = 0; (i) < (n); ++(i))
#define REPR(i, n) for (int(i) = (n); (i) >= 0; --(i))
#define FOR(i, n, m) for (int(i) = (n); (i) < (m); ++(i))

int main(){
    int n,a,b,cnt,tmp,ans;
    ans = 0;
    cin >>n>>a>>b;
    FOR(i,1,n+1){
        tmp = i, cnt = 0;
        REP(j,5){
            cnt+= tmp%10;
            tmp/=10;
        }
        if(a<= cnt && cnt <=b) ans+=i;
    }
    cout << ans << endl;
}
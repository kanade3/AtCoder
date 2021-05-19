#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define REP(i, n) for (int(i) = 0; (i) < (n); ++(i))
#define REPR(i, n) for (int(i) = (n); (i) >= 0; --(i))
#define FOR(i, n, m) for (int(i) = (n); (i) < (m); ++(i))
template <class T>
bool chmax(T &a, const T &b)
{
    if (a < b)
    {
        a = b;
        return true;
    }
    return false;
}
template <class T>
bool chmin(T &a, const T &b)
{
    if (a > b)
    {
        a = b;
        return true;
    }
    return false;
}

int main(){
    int n,a,ans,tmp;
    ans = 1001001001;
    cin >> n;
    REP(i,n){
        tmp = 0;
        cin>>a;
        while(a%2==0){
            ++tmp;
            a /= 2;
        }
        ans = min(ans,tmp);
    }
    cout << ans << endl;
}
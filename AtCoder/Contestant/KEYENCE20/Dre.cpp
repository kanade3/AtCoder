#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i < (n); ++i)
#define all(x) (x).begin(), (x).end()
#define ll = long long;
typedef pair<int,int>P;

const int INF = 1e18 +100;

int main(){
    int n;
    cin >> n;
    vector<P>a(n);
    rep(i,n){
        int x,len;
        cin >> x >> len;
        a[i].first=x+len;
        a[i].second=x-len;
    }
    // a.first(アーム右側を基準にソート)
    sort(all(a));
    int ans=0;
    int rr=-INF;
    rep(i,n){
        if(a[i].second>=rr){
            ++ans;
            rr=a[i].first;
        }
    }
    cout << ans << endl;
}

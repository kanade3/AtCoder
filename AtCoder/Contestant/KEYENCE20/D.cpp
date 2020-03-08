#include <bits/stdc++.h>
using namespace std;
using ll = long long;
 
#define REP(i,n) for(int i=0; i < (n); ++i)
#define REPR(i,n) for(int i=(n); i >= 0; --i)
#define FOR(i, m, n) for(int i = (m); i < (n); ++i)
 
#define INF 1e9
bool cmp(pair<ll, ll> l, pair<ll, ll> r){
  return l.first+l.second < r.first + r.second;
 
}
int main(){
  int N;
  cin >> N;
  vector<pair<ll, ll>> XL(N);
  REP(i, N){
    cin >> XL[i].first >> XL[i].second;
  }
  sort(XL.begin(), XL.end(), &cmp);
  ll ans = 0, pre = -INF-5;
  REP(i, N){
    cout << "XL" << XL[i].first << " " << XL[i].second << endl;
    if(pre <= XL[i].first - XL[i].second){
      ans++;
      pre = XL[i].first + XL[i].second;
      cout << i << " " << pre << endl;
    }
  }
  cout << ans << endl;
}
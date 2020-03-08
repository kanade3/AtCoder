#include <bits/stdc++.h>
#define rep(i,n) for (int i=0 ;i < (n); ++i)
using namespace std;
typedef long long ll;

const int mod = 1000000007;

struct mint {
  ll x; // typedef long long ll;
  mint(ll x=0):x((x%mod+mod)%mod){}
  mint operator-() const { return mint(-x);}
  mint& operator+=(const mint a) {
    if ((x += a.x) >= mod) x -= mod;
    return *this;
  }
  mint& operator-=(const mint a) {
    if ((x += mod-a.x) >= mod) x -= mod;
    return *this;
  }
  mint& operator*=(const mint a) {
    (x *= a.x) %= mod;
    return *this;
  }
  mint operator+(const mint a) const {
    mint res(*this);
    return res+=a;
  }
  mint operator-(const mint a) const {
    mint res(*this);
    return res-=a;
  }
  mint operator*(const mint a) const {
    mint res(*this);
    return res*=a;
  }
  mint pow(ll t) const {
    if (!t) return 1;
    mint a = pow(t>>1);
    a *= a;
    if (t&1) a *= *this;
    return a;
  }

  // for prime mod
  mint inv() const {
    return pow(mod-2);
  }
  mint& operator/=(const mint a) {
    return (*this) *= a.inv();
  }
  mint operator/(const mint a) const {
    mint res(*this);
    return res/=a;
  }
};
mint f(int n){
    if (n==0) return 1;
    mint x = f(n/2);
    x *=x;
    // f(x)=2^xのとき、f(2x)=f(x)^2,f(2x+1)=f(x)^2*2。こうすることで計算量がlognですむようになる。
    if (n%2==1) x*=2;
    return x;
}

mint choose(int n , int a){
    mint x =1 , y =1;
    rep(i,a){
        // 分子
        x *= n-i;
        // 分母
        y *= i+1;
    }
    return x / y;
}

int main(){
    int n,a,b;
    cin>> n>>a>>b;
    mint ans = f(n);
    ans -= 1;
    ans -= choose(n,a);
    ans -= choose(n,b);
    // mintは構造体なので.xを使って実体を参照する。
    cout << ans.x << endl;
    return 0 ;
}

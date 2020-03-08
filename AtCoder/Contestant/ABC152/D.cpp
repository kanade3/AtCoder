#include <bits/stdc++.h>
#define rep(i,n) for  (int i=0 ; i < (n); i++)
#define reps(i,n) for  (int i=1 ; i <= (n); i++)
#define pass (void)0
using namespace std;
typedef long long ll;
typedef pair<int,int>P;

P f(int x){
    //Topの桁を出す
    int a=x%10;
    int b=0;
    //Tailの桁を出す
    while (x){
        b=x;
        x/=10;
    }
    return P(a,b);
}

int main(){
    ll ans=0;
    int n;
    cin >> n;
    map<P,int> freq;
    reps(i,n){
        P p=f(i);
        freq[p]++;
    }
    reps(i,n){
        P p=f(i);
        P q(p.second,p.first);
        ans += freq[q];
    }
    cout << ans << endl;
}
#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ll N,K; cin >> N >> K;
    vector<int> a(N,0); for(int i = 0; i < N; i++) cin >> a.at(i);
    
    ll res = 0;
    ll sum = 0;
    int right = 0;
    for(int left = 0; left < N; left++){
        while(right < N && sum< K){
            sum += a.at(right);
            right++;
        }

        if(sum < K) break;
        res += N - right + 1;
        sum -= a.at(left);
    }
    cout << res << endl;
}


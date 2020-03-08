#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i,n) for  (int i=0 ; i < (n); i++)

int main(){
    int N;
    string s;
    cin>>N>>s;
    int e=0;
    int cnt=0;

    // 0ばんめがリーダーだった時を最初に数える
    rep(i,N){
        if(i==0){}
        else if(s[i]=='E')e++;
    }
    cnt=e;
    for(int i=1;i<N;i++){
        if(s[i-1]=='E')cnt--;
        if(s[i]=='W')cnt++;
        if(cnt<e)e=cnt;
    }
    cout<<e<<endl;
}
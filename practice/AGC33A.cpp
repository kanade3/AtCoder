#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)

int main(){
    int h,w,cnt=0;
    cin >> h >> w;
    vector<string> a(h);
    rep(i,h){
        cin >> a[i];
    }
    queue<pair<int,int>> q;
    int dx[]= {1,0,-1,0};
    int dy[]= {0,1,0,-1};
    vector<string> checker (h);

    rep(i,h){
        string s="";
        rep(j,w) s+="#";
        checker[i]=s;
    }

    rep(i,h) rep(j,w){
        if(a[i][j]=='#')q.push({i,j});
    }
    while(!q.empty()){
        if( a==checker ) break;
        vector<pair<int,int>> vec;
        while(!q.empty()){
            int y = q.front().first;
            int x = q.front().second;
            vec.push_back({y,x});
            q.pop();
        }
        rep(i,vec.size()) rep(j,4){
            int ny = vec[i].first + dy[j];
            int nx = vec[i].second + dx[j];
            if (0<= ny && ny<h && 0<=nx && nx < w && a[ny][nx]=='.'){
                a[ny][nx]='#';
                q.push({ny,nx});
            }
        }
        ++cnt;
    }
    cout << cnt << endl;



}
/*
a==checkerでcheckerとaが一致（全部#）してたらスキップ（一回も操作がいらないので）
*/
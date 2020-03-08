#include <bits/stdc++.h>
using namespace std;

const int dx[4] = {1,0,-1,0};
const int dy[4] = {0,1,0,-1};

int H,W;
vector<string> field;

bool seen[510][510];

void dfs(int h ,int w){
    seen[h][w]=true;

    // グリッド(4方向)を探索する
    for (int i=0;i<4;i++){
        int nh= h+dx[i];
        int nw= w+dy[i];

        //場外アウトは無視する
        if(nh<0 || nh>=H || nw<0 || nw>=W) continue;
        // 壁ならアウトなのでcontinue
        if(field[nh][nw]=='#') continue;

        // 探索済みの場合もcontinue
        if(seen[nh][nw]) continue;

        dfs(nh,nw);
    }
}

int main(){
    cin>>H>>W;
    field.resize(H);
    for(int h=0;h<H;h++){
        cin>>field[h];
    }
    // sとgのマスを探しておく
    int sh,sw,gh,gw;
    for(int h=0;h<H;h++){
        for(int w=0;w<W;w++){
            if(field[h][w]=='s') sw=w,sh=h;
            if(field[h][w]=='g') gw=w,gh=h;
        }
    }

    memset(seen,0,sizeof(seen)); //seenを全てfalseにする
    dfs(sh,sw);

    if (seen[gh][gw])  cout<<"Yes"<<endl;
    // gh,gwが探索済み==ゴールにたどり着けるルートが存在する
    else cout<<"No"<<endl;
}
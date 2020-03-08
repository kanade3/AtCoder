#include <bits/stdc++.h>
#define rep(i,n) for (int i=0;i<(n);++i)
using namespace std;
using ll = long long;

using Graph = vector<vector<int> >;

vector<int> tmpans(1);
// 深さ優先探索
vector<bool> seen;
void dfs(const Graph &G, int v,int fromo=-1,int fromt=-1) {
    seen[v] = true; // v を訪問済にする

    // v から行ける各頂点 next_v について
    for (auto next_v : G[v]) { 
        if (seen[next_v]) continue; // next_v が探索済だったらスルー

        if(fromo!=-1&&fromt!=-1){
            tmpans.push_back(fromo);
        }
        else if(fromo!=-1){
            dfs(G, next_v, fromo,v); 
        }
        else{
            dfs(G, next_v, v);
        }
    }
}

int main() {
    // 頂点数と辺数
    int N;
    cin >> N;

    vector<int> ans(N);

    // グラフ入力受取 (ここでは無向グラフを想定)
    Graph G(N);
    rep(i,N){
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
        G[b].push_back(a);
    }

    // 頂点 0 をスタートとした探索
    seen.assign(N, false); // 全頂点を「未訪問」に初期化
    dfs(G, 0);

    rep(i,tmpans.size()){
        cout << tmpans[i] << endl;
    }
}
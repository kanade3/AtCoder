#include <bits/stdc++.h>
using namespace std;
using Graph = vector<vector<int>>;

//DFS
vector<bool> seen;
void dfs(const Graph &G, int v)
{
    seen[v] = true; //探索済みにする

    //このvからいける頂点について考える
    for (auto next_v : G[v])
    {
        if (seen[next_v])
            continue;   // next_vが探索済みならスルーする
        dfs(G, next_v); //再帰
    }
}
// dfsのプログラム終了

int main()
{
    // 頂点数と辺数を入力する
    int N, M;
    cin >> N >> M;

    //グラフ入力受け取り
    Graph G(N);
    for (int i = 0; i < N; i++)
    {
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
        G[b].push_back(a);
    }

    //頂点を0として探索をスタートさせる
    seen.assign(N, false); //全頂点を探索していないに設定
    dfs(G, 0);
}
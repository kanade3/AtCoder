#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;
template <class T>
inline bool chmax(T &a, T b)
{
    if (a < b)
    {
        a = b;
        return 1;
    }
    return 0;
}
template <class T>
inline bool chmin(T &a, T b)
{
    if (a > b)
    {
        a = b;
        return 1;
    }
    return 0;
}
long long h[100010];

//DPテーブル
long long dp[10010];
const long long INF = 1LL << 60;

long long rec(int i)
{
    // DPの値が更新されていたら、そのままその値を返す
    if (dp[i] < INF)
        return dp[i];
    //足場0のコストは0
    if (i == 0)
        return 0;

    //i-1とi-2  上から計算する。足場N-1までのコストはN-2やN-3までの最小コストがわかってればわかるので、再帰関数を呼び出す。
    long long res = INF;
    chmin(res, rec(i - 1) + abs(h[i] - h[i - 1])); //足場i-1からきた場合
    if (i > 1)
        chmin(res, rec(i - 2) + abs(h[i] - h[i - 2])); //n-2からきた場合

    // 結果をメモしながら返す
    return dp[i] = res;
}

int main()
{
    int N;
    cin >> N;
    for (int i = 0; i < N; ++i)
        cin >> h[i];

    // 初期化 (最小化問題なので INF に初期化)
    for (int i = 0; i < 100010; ++i)
        dp[i] = INF;

    // 答え
    cout << rec(N - 1) << endl;
}
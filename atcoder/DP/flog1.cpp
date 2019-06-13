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

const long long INF = 1LL << 60;

int N;
long long h[10010];

//DPテーブル
long long dp[10010];

int main()
{
    int N;
    cin >> N;
    for (int i = 0; i < N; ++i)
        cin >> h[i];

    // INFに初期化
    for (int i = 0; i < N; ++i)
        dp[i] = INF;

    //最初の条件
    dp[0] = 0;
    //ノードN-1までのループ。
    for (int i = 1; i < N; ++i)
    {
        chmin(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]));
        //2以上なら2個前のものも確認する
        if (i > 1)
            chmin(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]));
    }

    cout << dp[N - 1] << endl;
}


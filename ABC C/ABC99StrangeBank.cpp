#include <iostream>
using namespace std;

int dp[100010];
int INF = 10000000;

int main()
{
    int N;
    cin >> N;

    // dp[0]の初期化
    dp[0] = 0;

    // dpの中身を初期化
    for (int i = 1; i <= 100000; i++)
    {
        dp[i] = INF;

        //6円でのDP計算
        int power = 1;
        while (power <= i)
        {
            dp[i] = min(dp[i], dp[i - power] + 1);
            power *= 6;
        }

        //9円でのDP計算
        power = 1;
        while (power <= i)
        {
            dp[i] = min(dp[i], dp[i - power] + 1);
            power *= 9;
        }
        
    }
    cout << dp[N] << endl;
    return 0;

    //DPは今の自分の値と計算値の比較を行うので、この場合minをとる必要がない
}
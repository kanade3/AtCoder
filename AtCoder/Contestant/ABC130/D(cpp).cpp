#include <bits/stdc++.h>
// 単純なn回ループを簡単に定義する
#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long ll;


int main()
{
    int n;
    ll k;
    cin >> n >> k;
    vector<int> a(n);
    rep(i, n)
    {
        cin >> a[i];
    }
    // しゃくとりのやつの中身の和sを定義
    ll s = 0;
    // 右側の添字をj
    int j = 0;
    ll ans = 0;
    // 左側は普通にループを回す

    rep(i, n)
    {
        //右端まで進める
        // 2,5,100,3 みたいに途中で満たさないものが含まれる時はこのループを飛ばす
        while (j < n && s + a[j] < k)
        {
            s += a[j];
            ++j;
        }
        ans += j - i;
        s -= a[i];
    }
    // 全体の部分列の個数はn+1C2個。全体から条件未満のものを引くことで、条件以上のものを探す
    ans = (ll)n * (n + 1) / 2 - ans;

    cout << ans << endl;

    return 0;
}
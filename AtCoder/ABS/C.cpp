#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define REP(i, n) for (int(i) = 0; (i) < (n); ++(i))
#define REPR(i, n) for (int(i) = (n); (i) >= 0; --(i))
#define FOR(i, n, m) for (int(i) = (n); (i) < (m); ++(i))
template <class T>
bool chmax(T &a, const T &b)
{
    if (a < b)
    {
        a = b;
        return true;
    }
    return false;
}
template <class T>
bool chmin(T &a, const T &b)
{
    if (a > b)
    {
        a = b;
        return true;
    }
    return false;
}

int main()
{
    char c;
    int cnt =0;
    REP(i,3){
        cin >> c;
        if(c == '1') cnt++;

    }
    cout << cnt << endl;
    return 0;
}
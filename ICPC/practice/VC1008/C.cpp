#include <bits/stdc++.h>
using namespace std;

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

int n;
vector<int> a;
vector<int> b(0);
string s;

int r[] = {5, 7, 5, 7, 7};

void solve()
{

    REP(i, n)
    {
        int r_index = 0;
        int tmp = 0;
        REP(j, n)
        {
            if (i + j >= n)
            {
                break;
            }
            tmp += a[i + j];
            if (tmp == r[r_index])
            {
                r_index++;
                tmp = 0;
            }
            else if (tmp > r[r_index])
            {
                break;
            }
            if (r_index == 5)
            {
                cout << i + 1 << endl;
                return;
            }
        }
    }
}

int main()
{
    while (1)
    {
        cin >> n;
        a.resize(n);
        if (n == 0)
        {
            return 0;
        }
        REP(i, n)
        {
            cin >> s;
            a[i] = s.length();
        }
        solve();
    }
}
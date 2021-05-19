#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define REP(i, n) for (int(i) = 0; (i) < (n); ++(i))
#define REPR(i, n) for (int(i) = (n); (i) >= 0; --(i))
#define FOR(i, n, m) for (int(i) = (n); (i) < (m); ++(i))

int main(){
    string s;
    cin >> s;
    bool ok = true;
    int cur = 0;
    s += "1111111";
    while(cur <= s.size()-1){
        string word;
        REP(i,5){
            word += s[cur+i];
        }
        // cout << word << endl;
        if(word=="11111") break;
        cur+=5;
        string tmp, tmp2;
        if(word=="dream"){
            tmp = s.substr(cur,2);
            tmp2 = s.substr(cur,5);
            if(tmp== "er"){
                if(tmp2!="erase"){
                    cur+=2;
                }
            }
        }
        else if(word=="erase"){
            tmp = s[cur];
            if(tmp == "r"){
                cur++;
            }
        }
        else{
            ok =false;
            break;
        }
    }
    if(ok){
        cout<<"YES"<<endl;
        return 0;
    }
    else {
        cout<<"NO"<<endl;
        return 0;
    }

}
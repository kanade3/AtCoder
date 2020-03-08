#include <bits/stdc++.h>
using namespace std;

int main(){
    int N,A;
    cin>>N>>A;

    int L=A;
    int R=A+N-1;
    int eat;
    // 絶対値が小さくなるように食べるが、この時に端が0かどうかで左端を食べるか、右端を食べるか、もしくは0を食べるかを決定する
    if (R<0) eat=R;
    else if (L>0) eat=L;
    else eat=0;

    //C++にはsum関数がないので工夫して和を求める。等差数列の和
    int answer=(L+R)*N/2-eat;

    cout<<answer<<endl;

    return 0;
}
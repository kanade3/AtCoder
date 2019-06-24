#include <vector>
#include <iostream>
using namespace std;



int main() {
  int n;
  cin>>n;
  vector<int>dp(100010);
  dp.at(0)=0;
  for(int n=1;n<=100000;n++){
    dp.at(n)=1<<30;
    int pow=1;
    while(pow<=n){
      dp[n]=min(dp[n],dp[n-pow]+1);
      pow*=6;
    }
    pow =1;
    while(pow<=n){
      dp[n]=min(dp[n],dp[n-pow]+1);
      pow*=9;
    }
  }
  cout << dp[n];
                
    
}

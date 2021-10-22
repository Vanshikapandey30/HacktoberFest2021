#include <iostream>
using namespace std;
int get_change(int m) {
  //write your code here
  //The goal in this problem is to find the minimum number
  // of coins needed to change the input value (an integer)
  // into coins with denominations 1, 5, and 10.
  int n = 0;
  int i;
  int coins[3] = {10, 5, 1};
  for(i = 0; i < 3; i++){
    while(m >= coins[i]){
        m = m - coins[i];
        n = n + 1;
    }
  }
 return n;

}

int main() {
  int m;
  cin >> m;
  int n = get_change(m);
  cout << n << '\n';
}

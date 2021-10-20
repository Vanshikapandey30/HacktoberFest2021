#include <iostream>
#include <vector>

using namespace std;

vector<int> optimal_summands(int n) {
  vector<int> summands;
  int i, cnt, curr_sum = 0;
  int curr = 0;
  //write your code here

  for(i = 1; i < n; i++){

    if(n - i > 0 && curr + i <= n ){
        n = n - i;
        cnt = cnt + 1;
        summands.push_back(i);
    }

  }
  return summands;
}

int main() {
  int n;
  cin >> n;
  vector<int> summands = optimal_summands(n);
  cout << summands.size() << '\n';
  for (size_t i = 0; i < summands.size(); ++i) {
   cout << summands[i] << ' ';
  }
}

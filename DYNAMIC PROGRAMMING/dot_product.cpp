#include <algorithm>
#include <iostream>
#include <vector>
using std::vector;

//Given two sequences a1,a2,...,an (ai is the profit per click of the i-th ad) and b1,b2,...,bn
//(bi is the average number of clicks per day of the i-th slot), we need to partition
//them into n pairs (ai,bj) such that the sum of their products is maximized.
long long max_dot_product(vector<int> a, vector<int> b) {
  // write your code here
  sort(a.begin(), a.end());
  sort(b.begin(), b.end());
  long long result = 0;
  for (size_t i = 0; i < a.size(); i++) {
    result += ((long long) a[i]) * b[i];
  }
  return result;
}

int main() {
  size_t n;
  std::cin >> n;
  vector<int> a(n), b(n);
  for (size_t i = 0; i < n; i++) {
    std::cin >> a[i];
  }
  for (size_t i = 0; i < n; i++) {
    std::cin >> b[i];
  }
  std::cout << max_dot_product(a, b) << std::endl;
}

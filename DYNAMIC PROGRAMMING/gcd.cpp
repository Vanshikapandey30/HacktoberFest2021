#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int gcd_naive(int a, int b) {
  int current_gcd = 1;
  for (int d = 2; d <= a && d <= b; d++) {
    if (a % d == 0 && b % d == 0) {
      if (d > current_gcd) {
        current_gcd = d;
      }
    }
  }
  return current_gcd;
}

long long int gcd_fast(long int a, long int b) {
 long long int gcd_calc = __gcd(a,b);
 return gcd_calc;
}
//28851538 1183019
int main() {
  long long int a, b;
  cin >> a >> b;
  long long int gcd_cal = gcd_fast(a, b);
  cout << gcd_cal<< endl;
  return 0;
}

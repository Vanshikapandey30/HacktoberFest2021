#include <iostream>
#include<math.h>
#include<bits/stdc++.h>

int fibonacci_sum_naive(long long n) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;
    long long sum      = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
        sum += current;
    }

    return sum % 10;
}

long long int fibonacci_sum_good(long long int n){
  //n is a very very long number
  //use pisano period
  // According to it fibonacci numbers occur in periods of 60

  n = (n + 2) % 60;
  int num[n + 1];
  int result = 1;
  int i;
  num[0] = 0;
  num[1] = 1;
  for(i = 2; i <= n; i++){
    num[i] = ((num[i - 1] % 10) + (num[i - 2] % 10))%10;

  }
  if(num[n] == 0){
    return 9;
  }
  else
  {
      return((num[n] % 10) - 1);
  }


}



int main() {
    long long n = 0;
    std::cin >> n;
    std::cout << fibonacci_sum_good(n);
}

#include <iostream>
#include<bits/stdc++.h>

long long int pisanoPeriod(long int m){

    int previous = 0;
    int current = 1;
    long int i;
    for(i = 0; i < m*m; i++){
         current = (previous + current) % m;
         previous = current;
         if(previous == 0 && current == 1){
        return i + 1;
    }

    }
}

long long get_fibonacci_huge_naive(long long n, long long m) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    return current % m;
}

long long int good_long_fibonacci(long long int n, long long int m){

    long int pisano_period =  pisanoPeriod(m);
    n  =  n % pisano_period;
    long int previous = 0;
    long int current = 1;
    if(n == 0){
        return 0;
    }
//2816213588 239
    else if(n == 1){
        return 1;
    }
    else {
    long int i;
    for(i = 0; i < n - 1 ; i++){
        current = previous + current;
        previous = current;
    }

    return (current % m);
    }
 }

//2816213588 239
int main() {
    long long int n, m;
    std::cin >> n >> m;
    std::cout << good_long_fibonacci(n, m) << '\n';
}

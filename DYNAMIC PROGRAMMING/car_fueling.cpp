#include <iostream>
#include <vector>
using namespace std;

int compute_min_refills(long long int dist,long long int tank, vector<long int>stops) {
    long int num_refill = 0;
    long int current_refill = 0;
    long int last_refill;
    long int n = stops.size();
    while(current_refill <= n){
            last_refill = current_refill;
    while(current_refill < n && stops[current_refill + 1] - stops[last_refill] <= dist){
      current_refill = current_refill + 1;
       if(current_refill == last_refill){
        return -1;
    }

    }

    if(current_refill <= n){
        num_refill = num_refill + 1;
    }
    }
    // write your code here
    return -1;
}


int main() {
    int d = 0;
    cin >> d;
    int m = 0;
    cin >> m;
    int n = 0;
    cin >> n;

    vector<long int> stops(n);
    for (size_t i = 0; i < n; ++i)
    {
        cin >> stops.at(i);
    }
    long int items =  compute_min_refills(d, m, stops);
    cout << items << "\n";

    return 0;
}


#include <bits/stdc++.h>
using namespace std;
typedef struct {
    double v;
    double w;
    double ratios;
}Items;
Items Item[10000];

bool comp(Items a,Items b){
     return(a.ratios > b.ratios);

}

double get_optimal_value(long int capacity, vector<double> weights, vector<double> values) {
  double value = 0.0;
  long int n = weights.size();
  long int i;
  for(i = 0; i < n; i++){
        Item[i].v = values[i];
        Item[i].w = weights[i];
        Item[i].ratios = (double)(values[i]/weights[i]);
  }
 sort(Item, Item + n, comp);
 i = 0;
 double curr = 0.0, weight = 0.0;

 for(i = 0; i < n; i++){
    if(weight + Item[i].w <= capacity)
    {
        value = value + Item[i].v;
        weight = weight + Item[i].w;
    }

    else
    {
        curr = capacity - weight;
        value = value + Item[i].v * ((double)curr / Item[i].w);
        break;
    }

 }
  // write your code here
return value;
}

int main() {
  long int n;
 long int capacity;
  cin >> n >> capacity;
  vector<double> values(n);
  vector<double> weights(n);
  for (int i = 0; i < n; i++) {
   cin >> values[i] >> weights[i];
  }

  double optimal_value = get_optimal_value(capacity, weights, values);

  //cout.precision(10);
  //cout << optimal_value << endl;
  printf("%.4f\n", optimal_value);
  return 0;
}

#include <iostream>
#include <vector>
using namespace std;

int optimal_weight(int W, vector<int> w) {
  //write your code here
  // allocate memory on heap
  // call stack restrictions cannot handle very huge 2d arrays
    int i, wt;
    long int n = w.size();
    int** weights= new int* [n + 1];

    for(int i = 0; i <= n; i++){
        weights[i] = new int[W + 1];
    }
	for (i = 0; i <= n; i++) {
		for (wt = 0; wt <= W; wt++) {
			if (i == 0 || wt == 0)
				weights[i][wt] = 0;
			else if(w[i - 1] <= wt)
				weights[i][wt] = max(
				w[i - 1] + weights[i - 1][wt - w[i - 1]],  weights[i - 1][wt]
				);
			else
				weights[i][wt] = weights[i - 1][wt];
		}
	}
	int result =  weights[n][W];
	for (int i = 0; i < n; i++) {
    delete[] weights[i];
  }

  delete[] weights;
  return result;

}

int main() {
 int n, W;
 cin >> W >> n;
 vector<int> w(n);
 for (int i = 0; i < n; i++) {
    cin >> w[i];
  }
 int res = optimal_weight(W, w);
 cout << res <<endl;
}

#include <iostream>
#include <vector>

using namespace std;;

long int lcs2(vector<long int> X, vector<long int> Y,long int m,long int n) {
    long int L[m + 1][n + 1];
    long int i, j;
    for (i = 0; i <= m; i++)
    {
        for (j = 0; j <= n; j++)
        {
        if (i == 0 || j == 0)
            L[i][j] = 0;

        else if (X[i - 1] == Y[j - 1])
            L[i][j] = L[i - 1][j - 1] + 1;

        else
            L[i][j] = max(L[i - 1][j], L[i][j - 1]);
        }
    }
    return L[m][n];
}

int main() {
  long int n;
  cin >> n;
  vector<long int> a(n);
  long int i;
  for (i = 0; i < n; i++) {
  cin >> a[i];
  }

  long int m;
  cin >> m;
  vector<long int> b(m);
  for (i = 0; i < m; i++) {
    cin >> b[i];
  }
  long int len = lcs2(a, b, n, m);
  cout << len << endl;
}

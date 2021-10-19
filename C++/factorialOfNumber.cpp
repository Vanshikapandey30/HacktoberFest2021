#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int ans = 1;

    while (n > 0)
    {
        ans = ans * n;
        n--;
    }
    cout << ans;
    return 0;
}

// fact of 5 -> 5*4*3*2*1 = 120

// i/p : 5
// o/p : 120

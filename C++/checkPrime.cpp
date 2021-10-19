#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    if (n == 0 or n == 1)
    {
        cout << "Neither Prime nor Composite";
        return 0;
    }

    int i = 2;
    while (i < n)
    {
        if (n % i == 0)
        {
            cout << "No, its not Prime";
            return 0;
        }
        i++;
    }
    cout << "Yes, its Prime";
    return 0;
}

// Dry Run

// i/p : 7
// o/p : Yes, its Prime

// i/p : 1 
// o/p : Neither Prime nor Composite

// i/p : 4
// o/p : No, its not Prime
#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    int n;
    cin >> t;
    while(t > 0){
        cin >> n;
        vector <long int> a;
        long int item;
        int i;
        for( i = 0; i < n; i++){
            cin >> item;
            a.push_back(item);
        }
        int c1 = (n - 1)/2;
        int c2 =  (n - 1)/2;
        for(i = 0; i < n; i ++){
            if(a[i + 1] - a[i] >= 0){
                c1 --;
            }
            else{
                a[i] = -1 * a[i];
            }
          }
         for( i = 0; i < n; i++){
            cout << a[i] <<" ";
        }
        cout <<endl;
        t = t - 1;
    }
}

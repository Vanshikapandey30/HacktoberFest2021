
#include<iostream>
using namespace std;

long int minCoins(long int coinList[],long int n,long int value) {
   long int coins[value+1];       //store minimum coins for value i

   if(value == 0)
      return 0;              //for value 0, it needs 0 coin

   coins[0] = 0;

   for (long int i=1; i<=value; i++)
      coins[i] = INT16_MAX;            //initially all values are infinity except 0 value

   for (long int i=1; i<=value; i++) {      //for all values 1 to value, find minimum values
      for (long int j=0; j<n; j++)
         if (coinList[j] <= i) {
            long int tempCoins = coins[i-coinList[j]];
         if (tempCoins != INT16_MAX && tempCoins + 1 < coins[i])
            coins[i] = tempCoins + 1;
      }
   }
   return coins[value];       //number of coins for value
}

int main() {
   long int coins[] = {1, 3, 4};
   long int n = 3, value;
   cin >> value;
   cout << minCoins(coins, n, value) ;
   return 0;
}

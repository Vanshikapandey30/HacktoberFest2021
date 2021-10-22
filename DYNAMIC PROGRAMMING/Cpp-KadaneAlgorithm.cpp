/* 

Kadane's Algorithm

Kadane's is generally used for finding the max Subarray from a given array.

-------------------------Time and Space------------------------

Time - O(n) 
Space - O(1)

---------------------------------------------------------------

*/

#include<bits/stdc++.h>
using namespace std;

int maxSubArray(vector<int>& nums) {
        
        int currentSum =nums[0], totalSum = nums[0];
        
        for(int i=1; i<nums.size(); i++) {
            
            //Current max sum is either the current element OR current element + Previous Maximum subarray)
            currentSum = max(nums[i], currentSum+nums[i]); 
            
            //If the current maximum array sum is greater than the global total. Update it
            totalSum = max(totalSum, currentSum);
        }

        return totalSum;
}

int main()
{
    ios_base::sync_with_stdio(false),cin.tie(NULL);

    // the number of terms in the array
    int n=0;
    cin>>n;

    vector<int> v(n);
    for(int i = 0 ; i < n ; i++) cin >> v[i];

    // the nth fibonacci term 
    cout<<maxSubArray(v);

    return 0;
}

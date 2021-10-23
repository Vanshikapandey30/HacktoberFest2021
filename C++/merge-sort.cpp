// Sorting algorithm: C++ program to sort numbers of an array
// Time complexity of O(nlog(n))
// Divide-And-Conquer algorithm
// It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.

// Name: Atharva Patil
// Github Profile link:  https://github.com/atharvapatil123 

#include <iostream>
using namespace std;

// The Merge() function is used for merging two halves, by sorting them initially and then merging them.
void Merge(int a[],int lb,int mid,int ub){
    int i=lb,k=lb,j=mid+1;
    int b[9];
    while(i<=mid&&j<=ub){
        if(a[i]<a[j]){
            b[k]=a[i];
            i++;
        }
        else{
            b[k]=a[j];
            j++;
        }
        k++;
    }
    if(i>mid){
        while(j<=ub){
            b[k]=a[j];
            j++;
            k++;
        }
    }
    else{
        while(i<=mid){
            b[k]=a[i];
            i++;
            k++;
        }
    }
    k=lb;
    while(k<=ub){
        a[k]=b[k];
        k++;
    }
}

// Divide step: Dividing the array into halves 
void MergeSort(int a[],int lb,int ub){
    if(lb<ub){
        int mid = (lb+ub)/2;
        MergeSort(a,lb,mid);
        MergeSort(a,mid+1,ub);
        Merge(a,lb,mid,ub);
    }
}


// Driver function
int main()
{   int a[9] = {15,5,2,7,21,11,-1,6,50};
    MergeSort(a,0,8);
    for(int i=0;i<9;i++){
        cout<<a[i]<<endl;
    }
    return 0;
}

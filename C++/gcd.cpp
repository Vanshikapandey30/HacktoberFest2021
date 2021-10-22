#include<iostream>
using namespace std;
int main()
{
    intnumOne, numTwo, mp;
    cout<<"Enter Two Numbers: ";
    cin>>numOne>>numTwo;
    if(numOne>numTwo)
        mp = numOne;
    else
        mp = numTwo;
    while(1)
    {
        if((mp%numOne == 0) && (mp%numTwo == 0))
            break;
        else
            mp++;
    }
    cout<<"\nLCM ("<<numOne<<", "<<numTwo<<") = "<<mp;
    cout<<endl;
    return 0;
}
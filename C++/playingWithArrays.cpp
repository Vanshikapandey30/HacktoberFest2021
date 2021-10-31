/*this is a simple game program where you can play with array(s) and perform different operations like
searching a element in an array with linear or binary search.
sorting the array with several sorting techniques.
split or add array(s)
*/
#include<iostream> 
#include<list>

using namespace std;
void print_array(int arr[], int n){
    cout << " {";
        for (int i = 0; i < n; i++)
        cout <<arr[i] <<"\t";
        cout <<"}"<<endl;
}
void linear_search(int arr[], int key, int n){
    int checker = 0;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == key)
        {
            checker+=1;
            cout << "your element is found at " << i + 1 << "position"<<endl;
        }
    }
    if (checker == 0)
        cout << "element is not present in the array";    
}

void binary_search(int arr[], int key, int n){
    int i,start,end;
    start = 0;
    end = n-1;
    int t=0;
    while (start <= end)
    {
        int mid = (start+end)/2;
        if(key > arr[mid])
        start = mid +1;
        else if (key<arr[mid])
            end = mid-1;
        else{
        printf("%d element is found at %d position in your array.",key,mid+1);
        break;
        }
    }
    if(start>end)
    printf("%d element is not found in your array.",key);
}
void swap(int *a, int *b){
    int temp=*a;
    *a=*b;
    *b=temp;
}
void Insertion_sort(int arr[],int n){
    for (int i = 1; i < n; i++)
    {
        int temp = arr[i];
        int j = i-1;
        while (temp<arr[j] && j>=0)
        {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = temp;
    }
    print_array(arr,n);
}
void Bubble_sort(int arr[],int n){
    int c=1;
    while (c<n)
    {
        for (int i = 0; i < n-c; i++)
        {
            if(arr[i]>arr[i+1])
            swap(&arr[i],&arr[i+1]);
        }
        c++;
    }
    print_array(arr,n);
}
void Selection_sort(int arr[], int n){
    for(int i=0;i<n-1;i++){
        for (int j = i+1; j < n; j++)
        {
            if(arr[j] < arr[i])
            swap(&arr[i],&arr[j]);
        }
    }
    print_array(arr,n);
}
void Merge_sort(int arr[], int left_half, int right_half){
   
    if(left_half < right_half){
        int mid = (left_half + right_half)/2;
        Merge_sort(arr, left_half , mid);
        Merge_sort(arr, mid+1, right_half);
        merge(arr, left_half, mid, right_half);
    }
}
void merge(int arr[], int left_half, int mid, int right_half){
    int n1 = mid-left_half+1;
    int n2 = right_half-mid;
    int arr1[n1];
    int arr2[n2];
    for (int i = 0; i < n1; i++)
        arr1[i] = arr[left_half+i];
    for (int i = 0; i < n2; i++)
        arr2[i] = arr[mid +1 +i];
    int i = 0;
    int j = 0;
    int k = left_half;
    while (i < n1 && j < n2){
        if (arr1[i]<arr2[j])
        {
            arr[k] = arr1[i];
            k++;
            i++;
        }
        else{
        arr[k] = arr2[j];
        k++;
        i++;
        }
    }
    while(i<n1){
        arr[k] = arr1[i];
        k++;
        i++;
    }
    while(j<n2){
        arr[k] = arr1[i];
        k++;
        i++;
    }
}
int searching(int arr[], int key, int n){
    cout << "please choose the prefered searching technique:\n1.Lineae Search\n2.Binary Search"<<endl;
        int search_choice;
        cin >> search_choice;
        switch (search_choice)
        {
        case 1:
            linear_search(arr, key, n);
            break;
        case 2:
            binary_search(arr, key, n);
            break;
        default:
            cout<< "Error! invalid choice please retry."<< endl;
            break;
        }
    return 0;
}
void sorting(int arr[], int n){
        cout << "please choose the prefered sorting technique:\n1.Selection Sort\n2.Insertion sort\n3.Bubble Sort\n4.Merge Sort" <<endl;
        int sort_choice;
        cin >> sort_choice;
        switch (sort_choice){
        case 1:
            Selection_sort(arr, n);
            break;
        case 2:
            Insertion_sort(arr, n);
            break;
        case 3:
            Bubble_sort(arr, n);
            break;
        case 4:
            Merge_sort(arr, 0, n-1);
            break;
        default:
            cout<< "Error! invalid choice please retry."<< endl;
        }
}
void edit_array(int arr[], int n){
    cout << "Edit options:\n1.Add more elements.\n2.Remove element."<< endl;
    int edit_array_options;
    cin >> edit_array_options;
    switch (edit_array_options){
        case 1:
        {
            cout << "your previous entered array:"<<endl;
            print_array(arr,n);
            cout << "how many elements you want to add?"<<endl;
            int extra_add;
            cin >> extra_add;
            int added_length =n + extra_add;
            cout << " enter the elements: "<< endl;
            for (int i = n; i < added_length; i++)
                cin >> arr[i];
            cout << "your final array: "<< endl;
            print_array(arr,added_length);
        }
            break;
        case 2:
        {
            print_array(arr,n);
            cout << "1. single element remove\n2. Multiple element remove"<< endl;
            int remove_choice;
            cin >> remove_choice;
            switch(remove_choice)
            { 
                case 1:
                {
                    cout << "enter the position of element you want to remove: "<< endl;
                    int remove_element;
                    cin >> remove_element;
                    for (int i = remove_element+1; i < n; i++)
                        arr[i] = arr[i+1];
            
                    cout << "your final array: "<< endl;
                    print_array(arr,n-1);
                }
                    break;
                case 2:
                {
                    cout << "enter number of elements you want to remove:"<< endl;
                    int number_of_elements;
                    cin >> number_of_elements;
                    cout << "enter positions of elements you want to remove:"<< endl;
                    int remove_elements_array[number_of_elements];
                    for (int i = 0; i < number_of_elements; i++)
                        cin >> remove_elements_array[i];
                    
                    list<int> remove_elements (remove_elements_array, remove_elements_array + number_of_elements);
                    for (int i = 0; i < number_of_elements; i++)
                        remove_elements.remove(remove_elements_array[i]);
                    print_array(arr, number_of_elements);
                }      
                break;
                default:
                cout<<"Error! wrong choice."<<endl;
            }     
        }
        break;
        default:
            cout<<"Error! wrong choice."<<endl;
    }
}

int main(void)
{
    cout<<"what's should I call you?"<<endl;
    string str;
    cin >> str;
    cout << "Hey! "<< str <<" WELCOME, to the game 'playing with arrays', firstly you need to enter your array and the then you can choose the desired game for your array.\nEnter the lenght of your array: "<< endl;

    int array_length;
    cin >> array_length;
    int arr[array_length];
    cout<< "Enter the "<<array_length<<" elements of your array:"<< endl;
    for (int i = 0; i < array_length; i++)
        cin >> arr[i];
    cout << "Your entered array:" << endl;
    print_array(arr,array_length);
    
    cout << "What do you want to do now?\n1.searching\n2.Sorting\n3.edit your array"<< endl;
    cout<<"Enter your choice:";
    int start_choice;
    cin >> start_choice;
    switch(start_choice)
    {
    case 1:
        cout << "Enter the element you want to search in your array: "<< endl;
        int key;
        cin >> key;
        searching(arr, key, array_length);
        break;

    case 2:
        sorting(arr, array_length);
        break;
            
    case 3:
        edit_array(arr, array_length);
        break;

    default:
        cout << "Error!!!! wrong choice please retry."<<endl;
    }

    return 0;
}
 

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


bool sortByFinish(const vector<int>& v1, const vector<int>& v2) {
    return v1[1] < v2[1];
}

int main()
{
    int n;
    cout << "Enter the number of activities: ";
    cin >> n;

    vector<vector<int>> result;
    vector<vector<int>> activity;

    cout << "Enter the start and finish time of activities\n";
    int start,finish;
    for(int i=0;i<n;i++)
    {
        vector<int> duration;
        cin >> start >> finish;
        duration.push_back(start);
        duration.push_back(finish);
        activity.push_back(duration);
    }

    sort(activity.begin(), activity.end(), sortByFinish);

    result.push_back(activity[0]);

    int j=0;
    for(int i=1;i<n;i++)
    {
        if(activity[i][0] >= activity[j][1])
        {
            result.push_back(activity[i]);
            j=i;
        }
    }

    for(int i=0;i<result.size();i++)
    {
        cout << "{" << result[i][0] << ", " << result[i][1] << "}\n";
    }

}
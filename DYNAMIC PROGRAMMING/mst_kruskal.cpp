#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> tree;//used to store sets
vector<int> size;//used for efficinecy
struct Node{
    int a,b,w;
    bool operator <(const Node &second){
        return w<second.w;
    }
};

void make_set(int v){
    tree[v] = v;
    size[v] = 1;
}

int find_set(int v){
    if(tree[v] == v){
        return v;
    }
    return tree[v] = find_set(tree[v]);
}

void make_union(int a, int b){
    a = find_set(a);
    b = find_set(b);
    if(a!=b){
        if(size[a] < size[b]){
            swap(size[a], size[b]);
        }
        tree[b] = a;
        size[a] += size[b];
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n;//Enter numbers of vertex
    cin>>n;
    int m;//Number of edges in the graph
    cin>>m;
    tree.resize(n);//Maximum numbers of nodes is the size of array
    size.resize(n);//Maximum numbers of elements in array is n
    vector<Node> graph(n);
    for(int i=0;i<n;i++){
        make_set(i);//Initally all nodes are different sets
    }
    int x,y,w;
    for(int i=0;i<m;i++){
        cin>>x>>y>>w;
        x--,y--; //Comment this line if graph is 0-index based
        graph.push_back({x,y,w});
    }
    int cost=0; //inital cost of mst is zero
    sort(graph.begin(),graph.end()); //the edges based on their weights
    
    for(auto v: graph){
        if(find_set(v.a) != find_set(v.b)){
            cost+=v.w;
            make_union(v.a, v.b);
        }
    }
    cout<<cost<<"\n";
    return 0;

    /*Example Input
    4 5
    1 2 7
    1 4 6
    4 2 9
    4 3 8
    2 3 6

    Output
    19 */
}
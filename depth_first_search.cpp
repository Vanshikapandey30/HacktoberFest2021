#include<iostream>
using namespace std;

struct Node{
    int data;
    Node*left,*right;
    Node(int val):data(val),left(nullptr),right(nullptr){}
};

void dfs(Node*root){
    if(root==nullptr) return ;
    dfs(root->left);
    cout<<root->data<<" ";
    dfs(root->right);
}

int main(){
    Node*root=new Node(1);
    root->left=new Node(2);
    root->right=new Node(3);
    dfs(root); // output 2 1 3
}

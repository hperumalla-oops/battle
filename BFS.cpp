#include <iostream>
#include <vector>
#include<queue>

#define V 3  // Number of vertices

using namespace std;



void BFS(vector<vector<int>> &adj, vector<int> vist, int source){
    queue<int> q;
    vist[source]=1;
    cout<<source<<" ";

    while(!q.empty()){
        int s=q.front();
        q.pop();
        cout<<s<<" ";

        for(int i=0; i<V; i++){
            if(adj[s][s]==1 && vist[i]==0){
                vist[i]==1;
                q.push(i);
            }
        }
    }
}

int main(){
    vector<vector<int>> adj(V, vector<int>(V,0));
    vector<int> vist (V,0);

    for(int i=0; i<V; i++){
        for(int j=0; j<V; j++){
            cout<<i<<" "<<j<<"? ";
            cin>>adj[i][j];
        }
    }

    cout << "Adjacency Matrix:\n";
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            cout << adj[i][j] << " ";
        }
        cout << endl;
    }

    cout<<"BFS Traversal:"<<endl;
    BFS(adj,vist,0);
}
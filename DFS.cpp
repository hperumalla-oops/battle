#include <iostream>
#include <vector>
#include <bits/stdc++.h>


#define V 3  // Number of vertices

using namespace std;


void DFSrec(vector<vector<int>> &adj, vector<bool> &vist, int source){
    vist[source]=true;
    cout<<source<<" ";

    for(int i=0; i<V; i++){
        if (adj[source][i]==1 && !vist[i])
            DFSrec(adj,vist,i);
    }

}
int main() {

    vector<vector<int>> adj(V, vector<int>(V,0));
    vector<bool> vist(V, false);

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

    cout << "DFS Traversal: ";
    DFSrec(adj, vist, 0);
    cout << endl;

    return 0;
}



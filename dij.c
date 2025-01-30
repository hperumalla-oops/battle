#include <stdio.h>
#include <limits.h>
#include <stdbool.h>

#define V 5  // Number of vertices

// Function to find the vertex with the minimum distance
int minDistance(int dist[], bool visited[]) {
    int min = INT_MAX, min_index = -1;

    for (int v = 0; v < V; v++) {
        if (!visited[v] && dist[v] <= min) {
            min = dist[v];
            min_index = v;
        }
    }
    return min_index;
}

// Dijkstra's algorithm function
void dijkstra(int graph[V][V], int src) {
    int dist[V]; // Distance array
    bool visited[V]; // Visited set

    // Initialize all distances as infinite and visited as false
    for (int i = 0; i < V; i++) {
        dist[i] = INT_MAX;
        visited[i] = false;
    }

    dist[src] = 0; // Distance of source to itself is 0

    // Find shortest path for all vertices
    for (int count = 0; count < V - 1; count++) {
        int u = minDistance(dist, visited); // Pick the minimum distance vertex
        visited[u] = true; // Mark it as processed

        // Update distances for adjacent vertices
        for (int v = 0; v < V; v++) {
            if (!visited[v] && graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    // Print the final distances
    printf("Vertex \t Distance from Source (%d)\n", src);
    for (int i = 0; i < V; i++) {
        printf("%d \t %d\n", i, dist[i]);
    }
}

// Main function
int main() {
    int graph[V][V] = {
        {0, 10, 0, 30, 100},
        {10, 0, 50, 0, 0},
        {0, 50, 0, 20, 10},
        {30, 0, 20, 0, 60},
        {100, 0, 10, 60, 0}
    };

    int src = 0; // Source vertex
    dijkstra(graph, src);

    return 0;
}

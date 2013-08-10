Dijkstras-Algorithm
-------------------

Implementations of the following algorithms:
* Breadth First Search (BFS)
* Computing Connected Components (CC) on an undirected graph
* Dijkstra's Shortest-Path (DSP) algorithm
* a library for the heap data structure

<br>
* * *
The use of the heap data structure gives Dijkstra's algorithm an `O(mlogn)` running time, where m is the number of edges and n is the number of vertices.

BFS, CC and DSP, they all expect an adjacency list, and vertices are assumed to have numeric IDs (starting from 1).
* On BFS and CC, the adjacency list is a dictionary where for a vertex v and every edge(v,w), there is an entry in that dictionary where the key is v and the value is a list of all w.
* On DSP, the adjacency list is a dictionary where for a vertex v and every edge(v,w) with weight j, there is an entry in that dictionary where the key is v and the value is a list of all tuples (w,j).

* * *

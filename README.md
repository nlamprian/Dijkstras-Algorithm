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

BFS, CC and DSP, they all expect an adjacency list.
* On BFS and CC, the adjacency list is a dictionary in the form `adj_list[vertex_i] = [vertex_2, vertex_3, ..., vertex_j, ...]`, where each pair `(vertex_i,vertex_j)` is an edge of the graph.
* On DSP, the adjacency list is a dictionary int the form `adj_list[vertex_i] = [(vertex_2,length_2), (vertex_3,length_3), ..., (vertex_j,length_j), ...]`, where each tuple `(vertex_i,vertex_j,length_j)` is an edge of the graph.

* * *
<br>
The code was tested on `Python 3.3.2`.

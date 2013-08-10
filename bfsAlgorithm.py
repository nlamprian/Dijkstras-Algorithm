''' Breadth First Search Algorithm
	Note: works on both undirected and directed graphs
    Input:  adj_list - a dictionary with vertices as keys,
                       and edges as values in the form of list of neighboring vertices
    	    s - source vertex
    Output: a set of all reachable vertices from the source vertex s '''

import sys

def BFS(adj_list,s):
	explored, frontier = {s}, [s]
	while frontier:
		v = frontier.pop(0)
		for w in adj_list[v]:
			if w not in explored:
				explored.add(w)
				frontier.append(w)
	return explored


if __name__ == "__main__":
	# Expects a file (adjacency list), and a source vertex
	if len(sys.argv) < 3: sys.exit("Error: No input filename or source vertex.")
	filename, s = sys.argv[1], int(sys.argv[2])

	adj_list = {}
	with open(filename, 'r') as f:
		for line in f:
			vertices = line.split()
			adj_list[int(vertices[0])] = [int(v) for v in vertices[1:]]

	explored = BFS(adj_list,s)
	print(explored)

''' Algorithm for computing the connected components of an undirected graph
    Input:  adj_list - a dictionary with vertices as keys,
                       and edges as values in the form of list of neighboring vertices
    Output: cc - a list of sets, where each set represents a connected component '''

import sys
from bfsAlgorithm import BFS

def connectedComponents(adj_list):
	explored, cc = set(), []
	for v in range(1,len(adj_list)+1):
		if v not in explored:
			c = BFS(adj_list,v)
			explored |= c
			cc.append(c)
	return cc


if __name__ == "__main__":
	# Expects a file (adjacency list)
	if len(sys.argv) < 2:
		sys.exit("Error: No input filename.")
	filename = sys.argv[1]

	adj_list = {}
	with open(filename, 'r') as f:
		for line in f:
			vertices = line.split()
			adj_list[int(vertices[0])] = [int(v) for v in vertices[1:]]

	ccs = connectedComponents(adj_list)
	print(ccs)
